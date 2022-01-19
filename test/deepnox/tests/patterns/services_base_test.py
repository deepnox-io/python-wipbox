#!/usr/bin/env python3

"""

Unit tests: `denier.denier.tests.base.services_base`.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.patterns.services_base import BaseService, BusinessService, ComputingService


class BaseServiceTestCase(unittest.TestCase):
    """
    {ComputingService} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(BaseService(), BaseService)


class BusinessServiceTestCase(unittest.TestCase):
    """
    {BusinessService} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(BusinessService(), BusinessService)


class ComputingServiceTestCase(unittest.TestCase):
    """
    {ComputingService} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(ComputingService(), ComputingService)


if __name__ == "__main__":
    unittest.main()
