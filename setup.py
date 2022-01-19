#!/usr/bin/env python3

"""
The setup script.

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.

"""
import sys
from distutils.core import Command

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__name__ = "deepnox-box-in-progress"
__version__ = "0.0.14"
VERSION = __version__


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
    name="deepnox-box-in-progress",
    version="{0}".format(VERSION),
    description="(denier.io) Listening tickers and computing OHLC for different exchanges.",
    license="Copyrighted 2021, Deepnox SAS",
    author="François Michaud, for Deepnox SAS",
    author_email="contact@deepnox.io",
    url="https://github.com/deepnox-io/pythpn-deepnox-bpx-in-progress",
    download_url="https://github.com/deepnox-io/pythpn-deepnox-bpx-in-progress/{0}.tar.gz".format(
        VERSION
    ),
    long_description="Listening tickers and computing OHLC for different exchanges.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: MIT",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "deepnox",
    ],
    packages=["deepnox"],
    package_dir={"deepnox": "src/deepnox"},
    scripts=[],
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={
        "test": RunUnitTests,
        # 'coverage': RunTestsCoverage,
        # 'upload': UploadCoverage
    },
)
