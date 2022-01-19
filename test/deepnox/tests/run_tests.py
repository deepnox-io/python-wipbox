import logging
import os
import sys
import unittest

from deepnox.loggers.formatters import JsonFormatter

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(JsonFormatter)
    logger.addHandler(handler)
    loader = unittest.TestLoader()
    tests = loader.discover(pattern="*_test.py",
                            start_dir=os.path.dirname(__file__))
    runner = unittest.runner.TextTestRunner()
    runner.run(tests)
