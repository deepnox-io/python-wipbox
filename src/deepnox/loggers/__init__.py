#!/usr/bin/env python3

"""
Package: deepnox.loggers

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

from . import defaults
from . import formatters 

import logging
import logging.config
import os

formatters = formatters

__import__("pkg_resources").declare_namespace(__name__)

# @see: https://gist.github.com/pmav99/49c01313db33f3453b22

# A regarder absolument:
# * https://towardsdatascience.com/8-advanced-python-logging-features-that-you-shouldnt-miss-a68a5ef1b62d
# * https://gist.github.com/mariocj89/73824162a3e35d50db8e758a42e39aab
# * Terminal colorized: https://gist.github.com/exhuma/8147910


# Define MESSAGE log level
AUDIT = 25

# "Register" new loggin level
logging.addLevelName(AUDIT, "AUDIT")  # addLevelName(25, 'MESSAGE')

# Verify
assert logging.getLevelName(AUDIT) == "AUDIT"


def audit(self, msg, *args, **kwargs):
    if self.isEnabledFor(AUDIT):
        self._log(AUDIT, msg, args, **kwargs)


logging.Logger.audit = audit

DEFAULT_LOGGER_NAME = "root" or os.environ.get("LG_LOGGER_NAME")
"""The default loggers name.
"""


def setup(config: dict = defaults.DEFAULT_LOG_SETTINGS):
    """Setup loggers from provided configuration as dict.

    :param config: The wished configuration for loggers.
    """
    logging.config.dictConfig(config=config)


def update_defaults_setup(config: dict = defaults.DEFAULT_LOG_SETTINGS):
    """Setup loggers from provided configuration as dict.

    :param config: The wished configuration for loggers.
    """
    config = {**defaults.DEFAULT_LOG_SETTINGS, **config}
    logging.config.dictConfig(config=config)


def factory(name: str = DEFAULT_LOGGER_NAME, suffix: str = None):
    """A simple loggers factory.

    :param name: The loggers name.
    :param suffix: Optional suffix loggers
    :return: An instance of official Python {logging.Logger}
    """
    if isinstance(suffix, str) and len(suffix) > 0:
        try:
            return logging.getLogger(name).getChild(suffix=suffix)
        except Exception:
            return logging.getLogger(name)
    return logging.getLogger(name)


def auditor(project_name: str):
    return factory(f"loadguard.tests.load.metrics.{project_name}")
