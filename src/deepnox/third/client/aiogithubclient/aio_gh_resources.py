#!/usr/bin/env python3

"""
Module: deepnox.third.client.aiogithubclients.aio_gh_client

This file is a part of python-deepnox-box-in-progress project.

(c) 2021, Deepnox SAS.
"""
import asyncio

from deepnox.aiorest.resources import Resource
from deepnox.network.http import HttpRequest


class RepositoriesResource(Resource):

    name = 'repositories'
    prefix = 'repositories'

    def all(self):
        print('----', self.absolute_endpoint_url(''))
        return HttpRequest(url=self.absolute_endpoint_url(''))
