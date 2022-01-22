#!/usr/bin/env python3

"""
Module: deepnox.helpers.testing_helpers

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import asyncio
import logging
import traceback
import unittest
from io import StringIO

LOGGER = logging.getLogger(__name__)
""" The module logger. """


class LogCaptureResult(unittest._TextTestResult):

    def _exc_info_to_string(self, err, test):
        # jack into the bit that writes the tracebacks, and add captured log
        tb = super(LogCaptureResult, self)._exc_info_to_string(err, test)
        captured_log = test.stream.getvalue()
        return '\n'.join([tb, 'CAPTURED LOG', '=' * 70, captured_log])


class LogCaptureRunner(unittest.TextTestRunner):

    def _makeResult(self):
        # be nice if TextTestRunner just had a class attr for defaultResultClass
        return LogCaptureResult(self.stream, self.descriptions, self.verbosity)


class _AssertNotRaisesContext(unittest.case._AssertRaisesContext):
    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            self.exception = exc_value.with_traceback(None)

            try:
                exc_name = self.expected.__name__
            except AttributeError:
                exc_name = str(self.expected)

            if self.obj_name:
                self._raiseFailure(f"{exc_name} raised by {self.obj_name}")
            else:
                self._raiseFailure(f"{exc_name} raised")

        else:
            traceback.clear_frames(tb)

        return True


class BaseTestCase(unittest.TestCase):
    """

    :credits: https://gist.github.com/clayg/3787160
    """

    def setUp(self, *args, **kwargs):
        super(BaseTestCase, self).setUp(*args, **kwargs)
        # create a in memory stream
        self.stream = StringIO()
        # add handler to LOGGER
        self.handler = logging.StreamHandler(self.stream)
        LOGGER.addHandler(self.handler)
        self.LOG = LOGGER.getChild(self.__class__.__name__)

    def tearDown(self, *args, **kwargs):
        super(BaseTestCase, self).tearDown(*args, **kwargs)
        # we're done with the capture handler
        if hasattr(self, "handler"):
            LOGGER.removeHandler(self.handler)

    def assertNotRaises(self, expected_exception, *args, **kwargs):
        context = _AssertNotRaisesContext(expected_exception, self)
        try:
            return context.handle('assertNotRaises', args, kwargs)
        finally:
            context = None


class BaseAsyncTestCase(BaseTestCase):
    """
    An helper to unit test :module:`asyncio` routines.

    """

    def setUp(self, *args, **kwargs):
        super(BaseTestCase, self).setUp(*args, **kwargs)
        self.loop = asyncio.get_event_loop()
