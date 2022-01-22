#!/usr/bin/env python3

"""

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.

"""

from deepnox import loggers
from deepnox.core.enumerations import UniqueEnum

LOGGER = loggers.factory(__name__)
""" The main LOGGER. """


class ContentType(UniqueEnum):
    """
    Non-exhaustive enumeration of content types.
    """

    APPLICATION__JSON = "application/json"
    """ The `application/json` content type. """

    APPLICATION__X_WWW_FORM_URLENCODED = "application/x-www-form-urlencoded"
    """ The `application/x-www-form-urlencoded` content type. """

    TEXT__PLAIN = "text/plain"
    """ The `text/plain` content type. """

    TEXT__HTML = "text/html"
    """ The `text/html` content type. """

    def __str__(self):
        return self.value
