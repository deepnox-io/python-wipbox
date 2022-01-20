#!/usr/bin/env python3

"""

Unit tests: `denier.denier.tests.base.denier.tests.models.denier.tests.base`.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import logging
import unittest

from deepnox.serializers.json_serializer import JsonSerializer

logging.basicConfig(level=logging.DEBUG)

JSON_OBJ = {'uid': 'uid_test', 'name': 'name_test', 'value': 1.43, 'active': True}
JSON_STR = '{"uid": "uid_test", "name": "name_test", "value": 1.43, "active": true}'


class JsonSerializerTestCase(unittest.TestCase):
    """
    Tests: {denier.denier.tests.base.denier.tests.models.denier.tests.base.Model}
    """

    def test____init__(self):
        self.assertIsInstance(JsonSerializer(), JsonSerializer)

    def test__dumps_a_dict(self):
        """
        Test: serialize an object
        """
        s = JsonSerializer().dump(JSON_OBJ)
        self.assertIsInstance(s, str)

    def test__loads_a_string(self):
        o = JsonSerializer().load(JSON_STR)
        self.assertIsInstance(o, dict)
        self.assertEqual(o.get('uid'), 'uid_test')
        self.assertEqual(o.get('name'), 'name_test')
        self.assertEqual(o.get('value'), 1.43)
        self.assertEqual(o.get('active'), True)

