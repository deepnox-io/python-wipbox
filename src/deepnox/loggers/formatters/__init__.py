#!/usr/bin/env python3

"""
Logging formatters.

Package: deepnox.loggers.formatters

Module: deepnox.loggers.defaults

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""


from .json_formatter import JsonFormatter
from .logstash_formatter import LogstashFormatter

__import__("pkg_resources").declare_namespace(__name__)
