#!/usr/bin/env python3

"""
Module: deepnox.tests.files.base

This file is a part of (deepnox.auth) project.

(c) 2021, Deepnox SAS.
"""

import unittest
from unittest import mock

from deepnox.files.base import get_all_files_recursively_from_directory


class GetRecursivelyFilesTestCase(unittest.TestCase):
    def test_list_recursively_files_from_unique_directory(self):
        with mock.patch("os.walk") as mockwalk:
            mockwalk.return_value = [
                ("/foo", ("bar",), ("baz.md",)),
                (
                    "/foo/bar",
                    (),
                    ("spam.txt", "eggs.properties", "chicken.conf"),
                ),
            ]
            self.assertEqual(
                len(get_all_files_recursively_from_directory("/foo")), 4
            )


if __name__ == "__main__":
    unittest.main()
