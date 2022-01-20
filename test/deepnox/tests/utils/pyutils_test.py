#!/usr/bin/env python3

"""
Unit tests: deepnox.tests.utils.pyutils

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.utils.pyutils import copy_func


class PyUtilsTestCase(unittest.TestCase):
    """
    Tests for {SingletonMeta}
    """

    def test__copy_func(self):
        """
        Test: copy a function.
        """
        def func1(*args, **kargs):
            if len(args) > 0:
                return args[0]
        func2 = copy_func(func1)
        self.assertEqual(func2.__code__.co_code, func1.__code__.co_code)

if __name__ == '__main__':
    unittest.main()
