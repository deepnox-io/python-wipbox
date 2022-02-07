#!/usr/bin/env python3

"""
The setup script.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.

"""

import sys
from types import FunctionType
from distutils.core import Command

__name__ = "wipbox"
""" The project name. """

__version__ = "0.0.14.2"
""" The current version (work in progress). """


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Cf. https://stackoverflow.com/a/23265673
try:
    from pypandoc import convert

    read_md: FunctionType = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found")
    read_md: FunctionType = lambda f: open(f, 'r').read()



with open("requirements.txt") as f:
    requires = f.readlines()
if sys.version_info[0] < 3 and sys.version_info[1] <= 6:
    raise Exception
else:
    tests_require = []
    test_command = [
        sys.executable,
        "-m",
        "pytest",
    ]  # Run unit tests
    coverage_command = [
        "coverage",
        "run",
        "-m",
        "pytest",
        "test/"
        "&&",
        "coverage",
        "report",
        "-m"
    ]  # Compute coverage
    coverage_xml = [
        "coverage",
        "xml",
    ]  # Export coverage as XML
    coverage_upload = [
        "codacy-coverage-reporter",
        "report",
    ]  # Upload to Codacity


class RunUnitTests(Command):
    """Run unit tests."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(test_command)
        raise SystemExit(errno)


class RunTestsCoverage(Command):
    """Run unit tests and report on code coverage using the 'coverage' tool."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(coverage_command)
        if errno == 0:
            subprocess.call(["coverage", "xml"])
        raise SystemExit(errno)


class UploadCoverage(Command):
    """Upload code coverage to Codacity."""

    user_options = []
    description = __doc__[1:]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        errno = subprocess.call(coverage_upload)
        if errno != 0:
            raise SystemExit(errno)


setup(
    name=__name__,
    version=f"{__version__}",
    description="A set of modern Python libraries under development to simplify the execution of reusable routines by different projects.",
    license="Copyrighted 2021-2022, Deepnox SAS",
    author="The Deepnox team",
    author_email="contact@deepnox.io",
    url="https://github.com/deepnox-io/pythpn-wipbox",
    download_url=f"https://github.com/deepnox-io/pythpn-wipbox/{__version__}.tar.gz",
    long_description=read_md("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "deepnox",
        "wipbox",
        "utilities",
        "tools",
        "various",
        "work in progress",
        "draft",
    ],
    packages=[
        "deepnox",
        "deepnox.aiobox",
        "deepnox.aiorest",
        "deepnox.auth",
        "deepnox.clients",
        "deepnox.core",
        "deepnox.files",
        "deepnox.helpers",
        "deepnox.loggers",
        "deepnox.loggers.formatters",
        "deepnox.models",
        "deepnox.network",
        "deepnox.patterns",
        "deepnox.repositories",
        "deepnox.serializers",
        "deepnox.settings",
        "deepnox.tests",
        "deepnox.tests.helpers",
        "deepnox.third",
        "deepnox.utils",
    ],
    package_dir={
        "deepnox": "src/deepnox",
        "deepnox.aiobox": "src/deepnox/aiobox",
        "deepnox.aiorest": "src/deepnox/aiorest",
        "deepnox.auth": "src/deepnox/auth",
        "deepnox.clients": "src/deepnox/clients",
        "deepnox.core": "src/deepnox/core",
        "deepnox.files": "src/deepnox/files",
        "deepnox.helpers": "src/deepnox/helpers",
        "deepnox.loggers": "src/deepnox/loggers",
        "deepnox.loggers.formatters": "src/deepnox/loggers/formatters",
        "deepnox.models": "src/deepnox/models",
        "deepnox.network": "src/deepnox/network",
        "deepnox.patterns": "src/deepnox/patterns",
        "deepnox.repositories": "src/deepnox/repositories",
        "deepnox.serializers": "src/deepnox/serializers",
        "deepnox.settings": "src/deepnox/settings",
        "deepnox.third": "src/deepnox/third",
        "deepnox.tests": "test/deepnox/tests",
        "deepnox.tests.helpers": "test/deepnox/tests/helpers",
        "deepnox.utils": "src/deepnox/utils",
    },
    scripts=[],
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={
        "test": RunUnitTests,
        'coverage': RunTestsCoverage,
        # 'upload': UploadCoverage
    },
)
