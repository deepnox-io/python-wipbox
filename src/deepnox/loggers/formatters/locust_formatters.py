#!/usr/bin/env python3

"""
A compatible logging formatter with `Locust <https://locust.io>`_ framework.

Module: deepnox.loggers.defaults

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import json
import logging
import re
import socket
import traceback
from datetime import datetime

from deepnox.utils.maps import Map


class JsonFormatter(logging.Formatter):
    """
    :see: https://github.com/israel-fl/python3-logstash/tree/master/logstash
    :todo: Fix settings!
    """

    def __init__(
        self,
        message_type='Logstash',
        tags=None,
        fqdn=False,
        settings: Map = None,
    ):
        """

        :param message_type:
        :param tags:
        :param fqdn:
        :param settings:
        """
        self.message_type = message_type
        self.tags = tags if tags is not None else []
        self.settings = settings

        if fqdn:
            self.host = socket.getfqdn()
        else:
            self.host = socket.gethostname()

    def get_extra_fields(self, record):
        # The list contains all the attributes listed in
        # http://docs.python.org/library/logging.html#logrecord-attributes
        skip_list = (
            'args',
            'asctime',
            'created',
            'exc_info',
            'exc_text',
            'filename',
            'funcName',
            'id',
            'levelname',
            'levelno',
            'lineno',
            'module',
            'msecs',
            'msecs',
            'message',
            'msg',
            'name',
            'pathname',
            'process',
            'processName',
            'relativeCreated',
            'thread',
            'threadName',
            'extra',
            'result',
        )

        easy_types = (str, bool, dict, float, int, list, type(None))

        fields = {}

        for key, value in record.__dict__.items():
            if key not in skip_list:
                if isinstance(value, easy_types):
                    fields[key] = value
                else:
                    fields[key] = repr(value)

        return fields

    def get_debug_fields(self, record):
        fields = {
            'stack_trace': self.format_exception(record.exc_info),
            'lineno': record.lineno,
            'process': record.process,
            'thread_name': record.threadName,
        }

        # funcName was added in 2.5
        if not getattr(record, 'funcName', None):
            fields['funcName'] = record.funcName

        # processName was added in 2.6
        if not getattr(record, 'processName', None):
            fields['processName'] = record.processName

        return fields

    @classmethod
    def format_source(cls, message_type, host, path):
        return '%s://%s/%s' % (message_type, host, path)

    @classmethod
    def format_timestamp(cls, time):
        tstamp = datetime.utcfromtimestamp(time)
        return (
            tstamp.strftime('%Y-%m-%dT%H:%M:%S')
            + '.%03d' % (tstamp.microsecond / 1000)
            + 'Z'
        )

    @classmethod
    def format_exception(cls, exc_info):
        return (
            ''.join(traceback.format_exception(*exc_info)) if exc_info else ''
        )

    @classmethod
    def serialize(cls, message):
        return json.dumps(message)

    def format_locust_stats_log(self, record):
        #  Name                                                          # reqs      # fails  |     Avg     Min     Max  Median  |   req/s failures/s
        # POST /alma-central/alma/callback/iv                          14
        # 0(0.00%)  |      65      46     219      47  |    0.90    0.00
        pattern = (
            '(?P<http_method>\\w+)\\s+'
            + '(?P<http_path>[^\\s]+)\\s+'
            + '(?P<reqs>\\d+)\\s+'
            + '(?P<fails>\\d+)\\((?P<fails_percent>[\\d\\.]+)\\%\\)\\s+'
            + '\\|\\s+'
            + '(?P<avg>\\d+)\\s+'
            + '(?P<min>\\d+)\\s+'
            + '(?P<max>\\d+)\\s+'
            + '(?P<median>\\d+)\\s+'
            + '\\|\\s+'
            + '(?P<requests_per_second>[\\d.]+)\\s+'
            + '(?P<failures_per_second>[\\d.]+)\\s+'
        )
        r = re.compile(pattern)
        data = [m.groupdict() for m in r.finditer(record.getMessage())]
        if len(data) > 0:
            http_method = data[0].get('http_method')
            if http_method in [
                'GET',
                'POST',
                'PUT',
                'DELETE',
                'OPTIONS',
                'HEAD',
            ]:
                data[0].update({'http_method': http_method})
            return 'locust statistics', data[0]
        return record.getMessage(), ''

    def format(self, record):
        msg_text = record.getMessage()
        # Create message dict
        message = {
            '@timestamp': self.format_timestamp(record.created),
            '@version': '1',
            'host': self.host,
            'path': record.pathname,
            'tags': self.tags,
            'type': self.message_type,
            # Extra Fields
            'level': record.levelname,
            'logger_name': record.name,
        }

        if record.name == 'locust.stats_logger':
            msg_text, statistics = self.format_locust_stats_log(record)
            if len(statistics) == '':
                return ''
            message.update({'message': msg_text, 'statistics': statistics})
        else:
            message.update({'message': record.getMessage()})

        # Add extra fields
        message.update(self.get_extra_fields(record))
        message.update(
            {
                'clients': self.settings.metadata.client,
                'app_name': self.settings.metadata.application.name,
                'app_version': self.settings.metadata.application.version,
                'test_uid': self.settings.metadata.test_uid,
            }
        )

        # If exception, add debug info
        if record.exc_info:
            message.update(self.get_debug_fields(record))

        return self.serialize(message)


# @see: https://gist.github.com/pmav99/49c01313db33f3453b22
