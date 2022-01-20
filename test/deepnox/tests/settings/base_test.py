#!/usr/bin/env python3

"""

Unit tests: deepnox.settings.base

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.settings.base import NotFoundConfigurationError


class NotFoundConfigurationErrorTestCase(unittest.TestCase):
    def test___init__(self):
        self.assertIsInstance(NotFoundConfigurationError(filename='/data/filename'), NotFoundConfigurationError)


if __name__ == '__main__':
    unittest.main()
