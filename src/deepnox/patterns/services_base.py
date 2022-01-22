#!/usr/bin/env python3

"""
Base classes and helpers used by deepnox.tests.services layer.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""


class BaseService(object):
    """
    A deepnox.tests.app class for logic & business deepnox.tests.services.
    """


class BaseAioService(BaseService):
    """ """

    def __init__(self, client: object, bearer_token: str = None):
        self.client = client
        self.bearer_token = bearer_token


class ComputingService(BaseService):
    """
    A deepnox.tests.app class for computing deepnox.tests.services.
    """

    def process(self):
        """
        Process the whished computing.
        """
        raise NotImplementedError("This coro `process` is not implemented.")


class BusinessService(BaseService):
    """
    A deepnox.tests.app class for business deepnox.tests.services.
    """
