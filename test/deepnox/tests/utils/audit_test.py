#!/usr/bin/env python3

"""
Unit tests: audit utilities.

This file is a part of (denier.io).

(c) 2021, Deepnox SAS.
"""
import logging
import unittest

from deepnox import loggers
from deepnox.utils.audit import timeit


class AuditUtilsTestCase(unittest.TestCase):
    """
    Audit utilities unit tests.
    """

    def test__timeit(self):
        @timeit(logger=logging.getLogger(__name__).getChild('audit'))
        def trace_test():
            for i in range(20000):
                pass

        def fn_testing_default_logging_info():
            trace_test()

        with self.assertLogs() as captured:
            fn_testing_default_logging_info()
        self.assertEqual(len(captured.records), 1)  # check that there is only one loggers message
        self.assertEqual(captured.records[0].getMessage(),
                         'Execution time: trace_test')  # and it is the proper one
        self.assertEqual(captured.records[0].levelname, 'INFO')
        print(captured.records[0].pathname)


if __name__ == '__main__':
    unittest.main()
