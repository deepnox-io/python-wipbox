import asyncio
import unittest

from deepnox.aiorest.client import BaseRestClient, RestClient
from deepnox.tests.aiorest.helpers.working_examples import BallDontLieClient


class BaseRestClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = BaseRestClient(
            loop=asyncio.get_event_loop(), base_url="https://url/"
        )

    def test_create_a_new_client(self):
        self.assertIsInstance(self.client, BaseRestClient)
        self.assertIsInstance(self.client.loop, asyncio.AbstractEventLoop)
        self.assertIsInstance(self.client.base_url, str)

    def test_create_a_inherited_class(self):
        # self.assertIsInstance(self.client, BallDontLieClient)
        self.assertIsInstance(self.client, BaseRestClient)


class RestClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RestClient(
            loop=asyncio.get_event_loop(), base_url="https://url/"
        )

    def test_list_services_from_client(self):
        self.assertEqual(len(self.client._resources), 0)


class WorkingExampleBallDontLieClientTestCase(unittest.TestCase):
    """
    Test cases to create HTTP REST clients in real life.
    """

    def test___init__(self):
        ball_dont_lie_client = BallDontLieClient(loop=asyncio.get_event_loop())
        self.assertIsInstance(ball_dont_lie_client, BallDontLieClient)


if __name__ == "__main__":
    unittest.main()
