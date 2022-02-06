#!/usr/bin/env python3

"""
Module: deepnox.third.client.aiogithubclients.aio_gh_client

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""
import asyncio

from deepnox.aiorest.client import RestClient


class GithubClient(RestClient):
    """
    https://www.balldontlie.io/#getting-started
    """

    def __init__(self, loop: asyncio.AbstractEventLoop = None,
                 username: str = None, token: str = None):



