#!/usr/bin/env python3

"""

Unit tests: `denier.denier.tests.base.denier.tests.models.denier.tests.base`.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import logging
import unittest

from deepnox.serializers.yaml_serializer import YamlSerializer

logging.basicConfig(level=logging.DEBUG)

YAML_OBJ = {'uid': 'uid_test', 'name': 'name_test', 'value': 1.43, 'active': True}
YAML_STR = """---
uid: uid_test
name: name_test
value: 1.43
active: true
"""


class YamlSerializerTestCase(unittest.TestCase):
    """
    Tests: {denier.denier.tests.base.denier.tests.models.denier.tests.base.Model}
    """

    def test____init__(self):
        self.assertIsInstance(YamlSerializer(), YamlSerializer)

    def test__dumps_a_dict(self):
        """
        Test: serialize an object
        """
        s = YamlSerializer().dump(YAML_OBJ)
        self.assertIsInstance(s, str)

    def test__loads_a_string(self):
        o = YamlSerializer().load(YAML_STR)
        self.assertIsInstance(o, dict)
        self.assertEqual(o.get('uid'), 'uid_test')
        self.assertEqual(o.get('name'), 'name_test')
        self.assertEqual(o.get('value'), 1.43)
        self.assertEqual(o.get('active'), True)

