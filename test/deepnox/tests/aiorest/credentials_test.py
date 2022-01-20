import unittest

from deepnox.aiorest.credentials import Credentials, BasicAuth


class CredentialsTestCase(unittest.TestCase):
    def test___init__(self):
        self.assertIsInstance(Credentials(), Credentials)


class BasicAuthTestCase(unittest.TestCase):
    def test___init__(self):
        self.assertRaises(TypeError, lambda: BasicAuth())
        self.assertRaises(TypeError, lambda: BasicAuth("username"))
        self.assertRaises(TypeError, lambda: BasicAuth(password="password"))
        self.assertIsInstance(BasicAuth("username", "password"), BasicAuth)
        self.assertIsInstance(BasicAuth("username", "password", encoding="utf8"), BasicAuth)

if __name__ == '__main__':
    unittest.main()
