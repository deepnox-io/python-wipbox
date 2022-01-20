#!/usr/bin/env python3

"""
A JSON serializer.

Package: deepnox.serializers.json_serializers

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""
import datetime
import json

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
        print("obj", type(obj))
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return arrow.get(obj).isoformat()
        elif isinstance(obj, (type)):
            return str(obj)
        elif isinstance(obj, (DeepnoxEnum)):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class JsonSerializer(BaseSerializer):
    """
    JSON record_serializer.
    """

    def __init__(self):
        """
        Crate a new JSON record_serializer.
        """
        super().__init__(name="json")

    def dump(self, o: object):
        """
        Serialize an object as JSON string.
        :param o: The object to serialize.
        :type o: object
        :return: The serializing object as string.
        :rtype: str
        """
        return json.dumps(o, cls=ComplexEncoder)

    def load(cls, s: str) -> object:
        """
        Unserialize a string from JSON.
        :param s: The string to unserialize.
        :type s: str
        :return: The unserializing string object as object.
        :rtype: str
        """
        return json.loads(s)
