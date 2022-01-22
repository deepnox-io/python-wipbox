#!/usr/bin/env python3

"""
A compatible logging formatter with LogStash.

Module: deepnox.loggers.formatters.logstash_formatter

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

from .json_formatter import JsonFormatter


class LogstashFormatter(JsonFormatter):
    """A Logstash formatter for loggers.

    :author: [Israel-FL](https://github.com/israel-fl/).
    :see: https://github.com/israel-fl/python3-logstash/tree/master/logstash
    """

    def __init__(self, message_type="Logstash", tags=None, fqdn=False):
        """Create an instance of JsonFormatter.

        :param message_type: Log type.
        :param tags: Optional related tags.
        :param fqdn: Optional FQDN.
        """
        super(LogstashFormatter, self).__init__(message_type, tags, fqdn)

    @classmethod
    def format_source(cls, message_type, host, path):
        """Format source of loggers as URI.

        :param message_type: The message type.
        :param host: The host.
        :param path: The path.
        :return: The formatted source as URI.
        """
        return "%s://%s/%s" % (message_type, host, path)

    def get_message(self, record):
        return {
            "@timestamp": self.format_timestamp(record.created),
            "@version": "1",
            "message": record.getMessage(),
            "host": self.host,
            "path": record.pathname,
            "tags": self.tags,
            "type": self.message_type,
            # Extra Fields
            "level": record.levelname,
            "logger_name": record.name,
        }
