#!/usr/bin/env python3

"""

Unit tests: deepnox.settings.base

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""

import unittest
from unittest import mock
from unittest.mock import mock_open

from deepnox.helpers.testing_helpers import BaseTestCase
from deepnox.settings.base import NotFoundConfigurationError, SettingsReader


class NotFoundConfigurationErrorTestCase(BaseTestCase):

    @mock.patch('os.path.isfile')
    def test___init__(self, mock_isfile):
        mock_isfile.return_value = False
        self.assertIsInstance(NotFoundConfigurationError(filename='/data/filename'), NotFoundConfigurationError)


class SettingsReaderTestCase(BaseTestCase):

    @mock.patch("os.path.isfile")
    @mock.patch("builtins.open", new_callable=mock_open, read_data="name: name_test\nvalue: 1.0")
    def test__create_an_instance_using_existing_file_should_be_okay(self, mock_file, mock_isfile):
        mock_isfile.return_value = True
        settings = SettingsReader('/path/to/settings')
        mock_file.assert_called_with('/path/to/settings', 'r')
        self.assertEqual("name_test", settings.name)

    def test__create_an_instance_using_existing_file_should_raise_an_error(self):
        self.assertRaises(NotFoundConfigurationError, lambda: SettingsReader('/path/to/settings'))


if __name__ == '__main__':
    unittest.main()
