#!/usr/bin/env python3

"""
Module: deepnox.loggers.formatters.yaml_formatter

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""


from deepnox.loggers.formatters.base_formatter import BaseFormatter
from deepnox.serializers.yaml_serializer import YamlSerializer


class YamlFormatter(BaseFormatter):
    def __init__(self, *args, fields=None, **kwargs):
        super().__init__(
            *args, fields=fields, serializer=YamlSerializer(), **kwargs
        )
