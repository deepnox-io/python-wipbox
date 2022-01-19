#!/usr/bin/env python3

"""
Unit tests: exceptions management utilities.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.utils.exceptions import raise_if_param_is_none


class ExceptionsUtilsTestCase(unittest.TestCase):
    """
    Exceptions management unit tests.
    """

    def test__exception_if_parameter_is_none(self):
        """
        Test: raise exception if parameter is None.
        :return:
        """
        self.assertFalse(raise_if_param_is_none(name='value_test'))
        self.assertRaises(TypeError, lambda: raise_if_param_is_none(name=None))
        self.assertFalse(raise_if_param_is_none(name='value_test', index='index_test'))
        self.assertRaises(TypeError, lambda: raise_if_param_is_none(name='value_test', index=None))



if __name__ == '__main__':
    unittest.main()
