#!/usr/bin/env python3

"""
Module: deepnox.tests.aiobox.base

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""
import asyncio
import unittest

from deepnox.aiobox.base import Task
from deepnox.helpers.testing_helpers import BaseTestCase

async def async_wait_test():
    await asyncio.sleep(0.5)


class TaskTestCase(BaseTestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def test_create_a_new_valid_task(self):
        self.assertIsInstance(Task(loop=self.loop, fn=async_wait_test), Task)


if __name__ == '__main__':
    unittest.main()
