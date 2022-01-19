import unittest


from deepnox.aiorest.resources import Resource
from deepnox.tests.aiorest.helpers.working_examples import PlayersResources


class ResourceTestCase(unittest.TestCase):
    def test_create_a_new_client(self):
        resource = PlayersResources()
        self.assertIsInstance(resource, Resource)

    def test_global_attributes(self):
        services = PlayersResources()
        self.assertEqual(services._attrs.get("name"), "players")
        self.assertEqual(services._attrs.get("prefix"), "players")
        self.assertEqual(len(services._attrs), 2)

    def test_if_a_none_rest_client_attribute_is_created(self):
        services = PlayersResources()
        self.assertIsNone(getattr(services, "client"))


if __name__ == "__main__":
    unittest.main()
