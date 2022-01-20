#!/usr/bin/env python3

"""

Unit tests: deepnox.network.content_types

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.network.content_types import ContentType


class ContentTypeTestCase(unittest.TestCase):

    def test__valididity_of_content_type(self):
        self.assertEqual(ContentType.APPLICATION__JSON, ContentType('application/json'))
        self.assertEqual(ContentType.APPLICATION__JSON.name, 'APPLICATION__JSON')
        self.assertEqual(ContentType.APPLICATION__JSON.value, 'application/json')
        self.assertEqual(str(ContentType.APPLICATION__JSON), 'application/json')


if __name__ == '__main__':
    unittest.main()
