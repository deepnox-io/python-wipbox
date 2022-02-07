import asyncio
from urllib.parse import urlencode

import aiohttp

from deepnox.aiorest.client import RestClient
from deepnox.aiorest.resources import Resource, run_as_async_request
from deepnox.network.http import HttpMethod
from deepnox.network.http import HttpRequest


class PlayersResources(Resource):
    name = 'players'
    prefix = "players"

    @run_as_async_request
    def filter(self, page: int = 0, per_page: int = 30, search: str = None):
        params = {
            "page": page,
            "per_page": per_page,
        }
        if search is not None: params['search'] = search
        params = urlencode(params)
        return HttpRequest(url=self.absolute_endpoint_url("") + "?" + params, method=HttpMethod.GET)

    @run_as_async_request
    def all(self):
        return HttpRequest(url=self.absolute_endpoint_url(""))


class TeamsServices(Resource):
    name = "teams"
    prefix = "teams"


class BallDontLieClient(RestClient):
    """
    https://www.balldontlie.io/#getting-started
    """

    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        super().__init__(loop=loop, base_url='https://www.balldontlie.io/api/v1',
                         base_http_headers={"Content-Type": "application/json"})

    players = PlayersResources()
    teams = TeamsServices()


async def main(client):
    x = await client._fetch(method=HttpMethod.GET, url="https://www.balldontlie.io/api/v1/players")




if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    client = BallDontLieClient(loop=loop)


    # r = loop.run_until_complete(main(client))
    #print("r1", r)
    r = loop.run_until_complete(client.players.filter(page=2))
    # r = loop.run_until_complete(main(client))
    print("r2", r)
    # r = loop.run_until_complete(client.players.all())
    # #r = loop.run_until_complete(main(client))
    # print("r3", r)
    # for o in client.history:
    #     if o is not None:
    #         print(o.to_dict())
