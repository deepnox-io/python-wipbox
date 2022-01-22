#!/usr/bin/env python3

"""

Module: deepnox.loggers.formatters.base_formatter

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import logging
import os
import socket
import traceback
from datetime import datetime
from typing import Any

from deepnox.serializers.base_serializer import BaseSerializer


def _value(record: logging.LogRecord, field_name_or_value: Any) -> Any:
    """
    Retrieve value from record if possible. Otherwise use value.
    :param record: The record to extract a field named as in field_name_or_value.
    :param field_name_or_value: The field name to extract from record or the default value to use if not present.
    """
    try:
        return getattr(record, field_name_or_value)
    except AttributeError:
        return field_name_or_value


class BaseFormatter(logging.Formatter):
    """
    The base class of extended logging formatter.
    """

    def __init__(
        self,
        *args,
        fields: dict = None,
        serializer: BaseSerializer = None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.fields: dict = fields or {}
        self._internal_serializer: BaseSerializer = serializer

        self.usesTime = lambda: "asctime" in self.fields.values()
        self.hostname = socket.gethostname()
        self.tags = self.fields.get("tags") or []

    # def format(self, record: logging.LogRecord):
    #     # Let python set every additional record field
    #     super().format(record)
    #     print(record)
    #
    #     message = {
    #         field_name: _value(record, field_value)
    #         for field_name, field_value in self.fields.items()
    #     }
    #     if isinstance(record.msg, collections.abc.Mapping):
    #         message.update(record.msg)
    #     else:
    #         message["msg"] = super().formatMessage(record)
    #
    #     if record.exc_info:
    #         message["exception"] = {
    #             "type": record.exc_info[0].__name__,
    #             "message": str(record.exc_info[1]),
    #             "stack": self.formatException(record.exc_info),
    #         }
    #
    #     return (
    #         super().formatMessage(record)
    #         if (len(message) == 1 and "msg" in message)
    #         else json.dumps(message)
    #     )

    def formatMessage(self, record: logging.LogRecord) -> str:
        # Speed up this step by doing nothing
        return ""

    def add_extra_fields(self, message, record: logging.LogRecord):
        """Add extra fields.

        :param message: Message to complete.
        :param record: The loggers record.
        :return: The formatted record.
        """
        message["extra"] = self.get_extra_fields(record)
        return message

    def format(self, record: logging.LogRecord):
        """Format record.

        :param record: The loggers record.
        :return: The formatted record.
        """
        record = BaseFormatter.get_short_path(record)
        content = self.get_message(record)
        content = self.add_extra_fields(content, record)
        content = self.add_debug(content, record)
        return self._internal_serializer.dump(content)

    @staticmethod
    def get_short_path(record: logging.LogRecord):
        """Return a short path.

        :param record: The loggers record.
        :return: The updated record including short path.
        """
        filename = os.path.basename(record.filename)
        if len(filename) > 20:
            filename = "{}~{}".format(filename[:3], filename[-16:])
        record.pathname = filename
        return record

    @classmethod
    def format_timestamp(cls, time):
        """Format a timestamp as ISO.

        :param time: Time to format.
        :return: The ISO formatted time.
        """
        ts = datetime.utcfromtimestamp(time)
        return (
            ts.strftime("%Y-%m-%dT%H:%M:%S")
            + ".%03d" % (ts.microsecond / 1000)
            + "Z"
        )

    @classmethod
    def format_exception(cls, exc_info: Exception):
        """Format a Python exception.

        :param exc_info: Exception.
        :return: The formatted exception.
        """
        if exc_info:
            trace = traceback.format_exception(*exc_info)
            if isinstance(trace, list) and trace[0] != "NoneType: None":
                return list(
                    filter(
                        lambda x: len(x) > 0,
                        map(lambda s: s.strip(), "".join(trace).split("\n")),
                    )
                )
        return

    def add_debug(self, message: str, record: logging.LogRecord):
        """If exception, add debug info.

        :param message: Message to complete.
        :param record: The loggers record.
        :return: The formatted record.
        """
        if record.exc_info:
            message["debug"] = self.get_debug_fields(record)
        return message

    def add_tag(self, message, record: logging.LogRecord):
        if len(self.tags) > 0:
            message["metadata"]["tags"] = self.tags
        return message

    def get_extra_fields(self, record: logging.LogRecord):
        """Returns extra fields of the provided loggers record.

        The list contains all the attributes listed in [Python loggers documentation](http://docs.python.org/library/logging.html#logrecord-attributes).

        :param record: The record.
        :return:
        """
        skip_list = (
            "args",
            "asctime",
            "created",
            "exc_info",
            "exc_text",
            "filename",
            "funcName",
            "id",
            "levelname",
            "levelno",
            "lineno",
            "module",
            "msecs",
            "msecs",
            "message",
            "msg",
            "name",
            "pathname",
            "process",
            "processName",
            "relativeCreated",
            "thread",
            "threadName",
            "stack_info",
        )

        easy_types = (str, bool, dict, float, int, list, type(None))

        fields = {}

        for key, value in record.__dict__.items():
            if key not in skip_list:
                if isinstance(value, easy_types):
                    fields[key] = value
                else:
                    try:
                        fields[key] = repr(value)
                    except TypeError as e:
                        fields[key] = "Unavailable representation: __repr__(self)"
        return fields

    def get_debug_fields(self, record: logging.LogRecord):
        """Returns debug fields of the provided loggers record.

        :record: The loggers record.
        :returns: debug fields of the provided loggers record.
        """
        fields = {
            "stack_trace": self.format_exception(record.exc_info),
            "lineno": record.lineno,
            "process": record.process,
            "thread_name": record.threadName,
        }

        # funcName was added in 2.5
        if not getattr(record, "funcName", None):
            fields["funcName"] = record.funcName

        # processName was added in 2.6
        if not getattr(record, "processName", None):
            fields["processName"] = record.processName

        return fields

    def get_message(self, record: logging.LogRecord):
        """Format record.

        :param record: The loggers record.
        :return: The formatted record.
        """
        # Create app message dict
        return {
            "date": self.format_timestamp(record.created),
            "message": record.getMessage(),
            "@timestamp": self.format_timestamp(record.created),
            "hostname": self.hostname,
            "logger_name": record.name,
            "level": record.levelname,
            "pathname": record.pathname,
        }

    def dump(self, message: object = None):
        """
        Serialize as message using `dump` coro of selected serializer.
        :param message: The record as dict.
        :type message: dict
        :return: The serialized log.
        :rtype: str
        """
        return self._internal_serializer.dump(message)
