#!/usr/bin/env python3
"""
# loadguard.tests.mock

This module provides mocks usable for testing.

(c) 2021, Deepnox SAS.

"""

from unittest import mock


class MockHttpResponse(object):
    """
    Mock a HTTP response.
    """

    def __init__(self, json_data, status_code: int = 200):
        """Create new instance of :class:`loadguard.tests.mock.MockHttpResponse`

        :param json_data: The request JSON data.
        :type json_data: str
        :param status_code: The mocked HTTP status code.
        :rtype status_code: [ int | str ]
        """
        self.json_data = mock.Mock(json_data)
        self.status_code = mock.Mock(status_code)

    def json(self) -> dict:
        """Returns HTTP response body.

        :return: The HTTP response body.
        :rtype: dict
        """
        return self.json_data
