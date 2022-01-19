#!/usr/bin/env python3

"""

Unit tests: `denier.denier.tests.base.repositories_base`.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest

import datetime as datetime

from deepnox.core.types import BooleanType, DateTimeType, StringType
from deepnox.models import BaseModel
from deepnox.repositories.repositories_base import (
    BaseRepository,
    ComputableRepository,
    Repository,
)


class BaseRepositoryTestCase(unittest.TestCase):
    """
    {BaseRepository} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(BaseRepository(), BaseRepository)


class RepositoryTestCase(unittest.TestCase):
    """
    {Repository} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(Repository(), Repository)


class FakeTickerModel(BaseModel):
    uid = str
    datetime = datetime
    exchange = str
    pair = str
    active = bool


class ComputableRepositoryTestCase(unittest.TestCase):
    """
    {Repository} denier.tests.base class tests.
    """

    def test_____init__(self):
        """
        Unit test: create new instance.
        :return:
        """
        self.assertIsInstance(ComputableRepository(model_cls=FakeTickerModel), ComputableRepository)

    def test__indexes(self):
        repo = ComputableRepository(model_cls=FakeTickerModel)
        self.assertIsInstance(repo, ComputableRepository)
        indexes = repo.indexes()
        self.assertEqual(indexes, ['datetime', 'exchange', 'pair'])

    def test__primary_keys(self):
        repo = ComputableRepository(model_cls=FakeTickerModel)
        self.assertIsInstance(repo, ComputableRepository)
        indexes = repo.primary_keys()
        self.assertEqual(indexes, ['datetime', 'exchange', 'pair'])


if __name__ == '__main__':
    unittest.main()
