#!/usr/bin/env python3

"""
Base classes and functions used by deepnox.tests.repositories.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import logging

import pandas as pd
from pandas import DataFrame

from deepnox import loggers

LOGGER: logging.Logger = loggers.factory(__name__)
loggers.setup()


class BaseRepository(object):
    """
    A deepnox.tests.app class for deepnox.tests.repositories.
    """


class Repository(BaseRepository):
    """
    A deepnox.tests.app class for () computable deepnox.tests.repositories.
    """


class ComputableRepository(BaseRepository):
    """
    A deepnox.tests.app class for () computable deepnox.tests.repositories.
    """

    LOG: logging.Logger = LOGGER.getChild("ComputableRepository")
    """ The class LOGGER. """

    def __init__(self, model_cls: object = None, input_data: object = None):
        self._model_cls = model_cls
        self._df: pd.DataFrame = pd.DataFrame()

    def indexes(self):
        """
        Return list containing indexes names.
        :return: The list containing indexes names.
        :rtype: list
        """
        return list(
            filter(
                lambda x: x is not False,
                [
                    v.index and k
                    for k, v in self._model_cls._attributes.items()
                ],
            )
        )  # :see: https://bit.ly/31KwLee

    def primary_keys(self):
        """
        Return list containing primary key(s) names.
        :return: The list primary key(s) names.
        :rtype: list
        """
        return list(
            filter(
                lambda x: x is not False,
                [
                    v.pk is True and k
                    for k, v in self._model_cls._attributes.items()
                ],
            )
        )  # :see: https://bit.ly/31KwLee

    def push(self, o: object = None):
        if o is None:
            self.LOG.error(
                f"A {type(None)} object provided to add to repository"
            )

        idx = []
        if isinstance(o, dict):
            idx = [o.get(self.index_name)]
            o.pop(self.index_name)
            o = [o]
        elif isinstance(o, list):
            idx = [o.get(self.index_name) and o.pop(self.index_name)]
        df = pd.DataFrame(o, index=[idx])
        self._df.append(df)
        return self

    def __dict__(self):
        pass

    def append(self, input_data: DataFrame):
        self.LOG.debug("input dztz = ", extra={"input_data": input_data})
        self.LOG.debug("input dztz = ", extra={"input_data": input_data})
        self._df.append(DataFrame.to_dict(input_data, orient="index"))
        self.LOG.debug("input dztz = ", extra={"self._df": self._df})

    @property
    def dataframe(self):
        return self._df

    def max_by_column(self, column):
        return self._df[column].max()

    def last(self):
        return self._df.iloc[-1]

    def __len__(self):
        """
        Return repository lengh.

        :return: Repository length.
        """
        return len(self._df)
