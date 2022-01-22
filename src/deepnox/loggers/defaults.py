#!/usr/bin/env python3

"""
Defaults settings used for logging.

Module: deepnox.loggers.defaults

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import sys

from deepnox.loggers.formatters.json_formatter import JsonFormatter
from deepnox.loggers.formatters.result_formatter import ResultFormatter
from deepnox.loggers.formatters.yaml_formatter import YamlFormatter

DEFAULT_LOG_SETTINGS = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "json_formatter": {
            "()": JsonFormatter,
        },
        "yaml_formatter": {
            "()": YamlFormatter,
        },
        "result_formatter": {
            "()": ResultFormatter,
        },
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "result_formatter",
            "level": "DEBUG",
            "stream": sys.stdout,
        }
    },
    "loggers": {
        "": {  # root loggers
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": True,
        },
        "__main__": {  # if __name__ == '__main__'
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
        "deepnox": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
        "loadguard": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
        "sncf.transilien": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
    "root": {"handlers": ["default"], "level": "INFO", "propagate": False},
}
