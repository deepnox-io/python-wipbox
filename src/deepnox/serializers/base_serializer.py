#!/usr/bin/env python3

"""
The base class for serializing services.

Package: deepnox.serializers.base_serializers

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""


class BaseSerializer(object):
    """
    A base class for record_serializer.
    """

    def __init__(self, name: str):
        """
        Create a new record_serializer.
        """
        self.name = name

    def dump(self, o: object):
        """
        Serialize an object as JSON string.
        :param s: The object to serialize.
        :type s: str
        :return: The serializing object as string.
        :rtype: str
        """
        raise NotImplementedError("`serialize` is not implemented")

    def load(self, s: str) -> object:
        """
        Unserialize a string from JSON.
        :param s: The string to unserialize.
        :type s: str
        :return: The unserializing string object as object.
        :rtype: str
        """
        raise NotImplementedError("`deserialize` is not implemented")
