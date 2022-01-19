#!/usr/bin/env python3

"""
Unit tests: denier.denier.tests.utils.oop

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.utils.oop import SingletonMeta


class SingletonMetaTestCase(unittest.TestCase):
    """
    Tests for {SingletonMeta}
    """

    def test__create_singleton(self):
        """
        Test: create singleton
        """
        class Singleton(metaclass=SingletonMeta):
            def __init__(self, name):
                self.name = name
        singleton_x = Singleton('name_test')
        singleton_y = Singleton('name_test')
        self.assertIsInstance(singleton_x, Singleton)
        self.assertIsInstance(singleton_y, Singleton)
        self.assertEqual(singleton_x, singleton_y)
        self.assertEqual(singleton_x.name, singleton_y.name)

        singleton_x.name = 'changed_name_test' # Change name value on X instance
        self.assertEqual(singleton_y.name, 'changed_name_test') # Check if Y instance has the same changed name.

if __name__ == '__main__':
    unittest.main()
