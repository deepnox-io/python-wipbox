#!/usr/bin/env python3

"""

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""

import os
import sys

__import__("pkg_resources").declare_namespace(__name__)

# Very important to run unit test in JetBrains PyCharm or Idea...
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
)
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "test")
)
