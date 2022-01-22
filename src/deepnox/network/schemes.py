#!/usr/bin/env python3

"""
Module: deepnox.network.schemes

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""


from deepnox.core.enumerations import UniqueEnum


class Scheme(UniqueEnum):
    """
    Unexhaustive enumeration of schemes.
    """

    FILE = "file"
    """ The file scheme. """

    HTTP = "network"
    """ The HTTP scheme. """

    HTTPS = "https"
    """ The HTTPS scheme. """

    FTP = "ftp"
    """ The FTP scheme. """

    FTPS = "ftps"
    """ The FTPS scheme. """

    WEBSOCKET = "ws"
    """ The websocket scheme. """

    SSH = "ssh"
    """ The SSH scheme. """

    GIT = "git"
    """ The git scheme. """

    def __str__(self):
        return self.value
