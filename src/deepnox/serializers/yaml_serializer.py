#!/usr/bin/env python3

"""
A YAML serializer.

Package: deepnox.serializers.yaml_serializers

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
from typing import Any

import yaml

from deepnox.serializers.base_serializer import BaseSerializer


def is_yaml(s):
    """
    Return True if provided string is a yaml object.
    :param s: The string to test.
    :return: True if yaml. False else.
    """
    try:
        yaml.load(s, Loader=yaml.FullLoader())
    except ValueError:
        return False
    return True


class YamlSerializer(BaseSerializer):
    """
    yaml record_serializer.
    """

    def __init__(self, encoder: Any = None):
        """
        Crate a new yaml record_serializer.
        """
        super().__init__(name="yaml", encoder=encoder)

    def dump(self, o: object):
        """
        Serialize an object as yaml string.
        :param o: The object to serialize.
        :type o: object
        :return: The serializing object as string.
        :rtype: str
        """
        return yaml.dump(o)

    def load(self, s: str) -> object:
        """
        Unserialize a string from yaml.
        :param s: The string to unserialize.
        :type s: str
        :return: The unserializing string object as object.
        :rtype: str
        """
        return yaml.load(s, Loader=yaml.FullLoader)
