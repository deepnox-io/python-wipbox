#!/usr/bin/env python3

"""
Module: deepnox.tests.network.urls_test

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import unittest

from deepnox.network import Scheme
from deepnox.network.http import HttpMethod
from deepnox.network.urls import Url
from deepnox.third import pydantic


class UrlTestCase(unittest.TestCase):
    """
    Test cases for :class:`deepnox.network.url.Url`
    """

    def test__create_url_without_parameter_should_be_valid(self):
        self.assertIsInstance(Url(), Url)

    def test__creating_an_url_passing_some_parameters_should_be_valid(self):
        """
        :todo: to fix
        """
        url = Url(host="example.org", path="api/1")
        self.assertIsInstance(url, Url)
        self.assertEqual("example.org", url.host)
        self.assertEqual("api/1", url.path)

    def test__a_unknown_attribute_should_raise_an_error(self):
        self.assertRaises(pydantic.error_wrappers.ValidationError, lambda: Url(method=HttpMethod.GET, host="example.org", path="api/1"))

    def test__each_attribute_should_be_registered_by_metaclass(self):
        url = Url(host="example.org", path="api/1", params={"name": "name_test", "value": "value_with_spécial_char$_to_test_urlencode"})
        self.assertIsInstance(url, Url)
        self.assertEqual("example.org", url.host)
        self.assertEqual("api/1", url.path)
        self.assertEqual({"name": "name_test", "value": "value_with_spécial_char$_to_test_urlencode"}, url.params)

    def test__url_with_querystring_params_to_string(self):
        url = Url(scheme=Scheme.HTTPS, host="example.org", path="api/1", params={"name": "name_test", "value": "value_with_spécial_char$_to_test_urle n çod€"})
        self.assertEqual("https://example.org/api/1?name=name_test&value=value_with_sp%C3%A9cial_char%24_to_test_urle+n+%C3%A7od%E2%82%AC", str(url))


    def _test__url_attributes_defined_after_instantiation_of_the_URL_class_should_not_have_a_slash_character_at_the_start_or_end_of_the_string(
            self,
    ):
        """
        :todo: to fix
        """
        url = Url(
            method=HttpMethod.GET, host="/example.org/", path="/api/1/"
        )
        self.assertEqual("example.org", url.host)
        self.assertEqual("api/1", url.path)


if __name__ == "__main__":
    unittest.main()
