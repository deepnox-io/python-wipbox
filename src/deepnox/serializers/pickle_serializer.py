#!/usr/bin/env python3

"""
A serializer for native Python pickle format.

Package: deepnox.serializers.pickle_serializers

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

from deepnox.serializers.base_serializer import BaseSerializer


class PickleSerializer(BaseSerializer):
    """
    yaml record_serializer.
    """

    def __init__(self):
        """
        Crate a new yaml record_serializer.
        """
        super().__init__(name="pickle")

    def dump(self, o: object):
        """
        Serialize an object as yaml string.
        :param o: The object to serialize.
        :type o: object
        :return: The serializing object as string.
        :rtype: str
        """
        pass

    def load(self, s: str):
        pass
