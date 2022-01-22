#!/usr/bin/env python3

"""
Create temporary file during unit testing.

:see: https://stackoverflow.com/a/54053967

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.


"""

import os
import tempfile


class TestFileContent(object):
    def __init__(self, content):
        self.file = tempfile.NamedTemporaryFile(mode="w", delete=False)

        with self.file as f:
            f.write(content)

    @property
    def filename(self):
        return self.file.name

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        os.unlink(self.filename)
