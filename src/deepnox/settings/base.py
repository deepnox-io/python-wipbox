#!/usr/bin/env python3

"""
This module offers features facilitating configuration management.

Module: deepnox.settings.base

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import os

import yaml

from deepnox import loggers
from deepnox.core.base import DeepnoxDict
from deepnox.utils.maps import UpperMap, Map

LOGGER = loggers.factory(__name__)
""" The module LOGGER. """


class NotFoundConfigurationError(IOError):
    """
    An exception if configuration can't be found.
    """

    def __init__(self, filename: str, message="{filename} is not found"):
        """
        Create a new instance of {NotFoundConfigurationError}
        :param filename:
        :param message:
        """
        self.filename: str = filename
        self.message: str = message.format(filename=self.filename)
        super().__init__(self.message)


def read_yaml_file(filename: str):
    """
    Open and read a YAML file.
    :param filename: The filename to deserialize.
    :return: The YAML object.
    """
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            LOGGER.error(
                f"Error while reading yaml file: {filename}", exc_info=exc
            )


def load_settings(filename: str = None):
    """
    Create a new settings object from provided configuration (a YAML file).
    :param filename: The configuration filename.
    """
    if filename is None or os.path.isfile(filename) is False:
        raise NotFoundConfigurationError(filename=filename)
    return Map(read_yaml_file(filename))

