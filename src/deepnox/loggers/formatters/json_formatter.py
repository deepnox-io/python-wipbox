#!/usr/bin/env python3

"""
Module: deepnox.loggers.formatters.json_formatter

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from deepnox.loggers.formatters.base_formatter import BaseFormatter
from deepnox.serializers.json_serializer import JsonSerializer


class JsonFormatter(BaseFormatter):
    def __init__(self, *args, fields=None, **kwargs):
        super().__init__(
            *args, fields=fields, serializer=JsonSerializer(), **kwargs
        )
