#!/usr/bin/env python3

"""
A logging formatter for load testing results.

Module: deepnox.loggers.formatters.result_formatter

:todo: To externalize to LoadGuard.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import logging

from deepnox.loggers.formatters.json_formatter import JsonFormatter


class ResultFormatter(JsonFormatter):
    def __init__(self, *args, fields=None, **kwargs):
        super().__init__(*args, fields=fields, **kwargs)

    def add_extra_fields(self, message, record: logging.LogRecord):
        """Add extra fields.

        :param message: Message to complete.
        :param record: The loggers record.
        :return: The formatted record.
        """
        message["result"] = self.get_extra_fields(record)
        return message
