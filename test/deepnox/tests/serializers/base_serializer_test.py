#!/usr/bin/env python3

"""

Unit tests: deepnox.serializers.base_serializer

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import logging
import unittest

from deepnox.serializers.json_serializer import BaseSerializer

logging.basicConfig(level=logging.DEBUG)

JSON_OBJ = {'uid': 'uid_test', 'name': 'name_test', 'value': 1.43, 'active': True}
JSON_STR = '{"uid": "uid_test", "name": "name_test", "value": 1.43, "active": true}'


class BaseSerializerTestCase(unittest.TestCase):
    """
    Tests: {denier.denier.tests.base.denier.tests.models.denier.tests.base.Model}
    """

    def test____init__(self):
        self.assertIsInstance(BaseSerializer(name='test'), BaseSerializer)

    def test__dumps_a_dict(self):
        """
        Test: serialize an object
        """
        self.assertRaises(NotImplementedError, lambda: BaseSerializer("name").dump(JSON_OBJ))


    def test__loads_a_string(self):
        self.assertRaises(NotImplementedError, lambda: BaseSerializer("name").load(JSON_STR))

