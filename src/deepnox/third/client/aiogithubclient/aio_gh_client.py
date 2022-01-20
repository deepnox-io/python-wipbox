#!/usr/bin/env python3

"""
Module: deepnox.third.client.aiogithubclients.aio_gh_client

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""
import asyncio

from deepnox.aiorest.client import RestClient
from deepnox.aiorest.credentials import BasicAuth
from deepnox.third.client.aiogithubclient.aio_gh_resources import RepositoriesResource


class GithubClient(RestClient):
    """
    https://www.balldontlie.io/#getting-started
    """

    def __init__(self, loop: asyncio.AbstractEventLoop = None,
                 username: str = None, token: str = None):
        super().__init__(loop=loop, base_url='https://api.github.com',
                         base_http_headers={'Content-Type': 'application/json'},
                         credentials=BasicAuth(username, token),
                         )

    repositories = RepositoriesResource()
    """ The repositories API resource group. """

async def async_main(client):
    res = await client.repositories.all()
    print(res)
    return res

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = GithubClient(loop)
    loop.run_until_complete(async_main(client))
