#!/usr/bin/env python3

"""
A JSON serializer.

Package: deepnox.serializers.json_serializers

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import datetime
import json
import sys

from deepnox.core.enumerations import DeepnoxEnum
from deepnox.serializers.base_serializer import BaseSerializer
from deepnox.third import arrow


def is_json(s):
    """
    Return True if provided string is a JSON object.
    :param s: The string to test.
    :return: True if JSON. False else.
    """
    try:
        json.loads(s)
    except ValueError:
        return False
    return True


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return arrow.get(obj).isoformat()
        elif isinstance(obj, arrow.Arrow):
            return obj.isoformat()
        elif isinstance(obj, (type, DeepnoxEnum)):
            return str(obj)
        else:
            try:
                return json.JSONEncoder.default(self, obj)
            except TypeError as e:
                return str(obj)


class JsonSerializer(BaseSerializer):
    """
    JSON record_serializer.
    """

    def __init__(self, encoder: json.JSONEncoder = None):
        """
        Crate a new JSON record_serializer.
        """
        if encoder is None:
            encoder = ComplexEncoder
        super().__init__(name="json", encoder=encoder)

    def dump(self, o: object):
        """
        Serialize an object as JSON string.
        :param o: The object to serialize.
        :type o: object
        :return: The serializing object as string.
        :rtype: str
        """
        return json.dumps(o, cls=self.encoder)

    def load(cls, s: str) -> object:
        """
        Unserialize a string from JSON.
        :param s: The string to unserialize.
        :type s: str
        :return: The unserializing string object as object.
        :rtype: str
        """
        return json.loads(s)
