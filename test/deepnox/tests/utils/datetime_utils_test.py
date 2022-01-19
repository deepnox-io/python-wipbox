#!/usr/bin/env python3

"""
Tests of datetime denier.tests.utils.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import datetime
import unittest

import arrow

from deepnox.utils.datetime_utils import get_dtkey


class DateTimeUtilsTestCase(unittest.TestCase):

    def test_get_dtkey(self):
        """
        Test: getting the `dtkey` for a provided datetime.
        :return:
        """
        self.assertEqual(get_dtkey(datetime.datetime(year=2021, month=10, day=20, hour=15, minute=2)), "202110201502")


if __name__ == '__main__':
    unittest.main()
