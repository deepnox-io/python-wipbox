import unittest

from deepnox.utils.strings_utils import remove_slash_at_start_and_at_end, extract_idp_code


class RemoveSlashAtStartAndAtEndTestCase(unittest.TestCase):

    def test__passing_string_including_slash_should_be_valid(self):
        self.assertEqual("poulet", remove_slash_at_start_and_at_end("/poulet"))
        self.assertEqual("poulet", remove_slash_at_start_and_at_end("/poulet/"))
        self.assertEqual("poulet", remove_slash_at_start_and_at_end(" /poulet/ "))
        self.assertEqual("pou/let", remove_slash_at_start_and_at_end(" /pou/let/ "))

    def test__passing_none_string_should_return_none(self):
        self.assertIsNone(remove_slash_at_start_and_at_end(None))


class ExtractIdpCodeTestCase(unittest.TestCase):

    def test__passing_string_including_idp_code_should_be_valid(self):
        self.assertEqual("9d7ff726-32c0-461f-addf-369cd4a4a3b7", extract_idp_code("I am a string containing an (9d7ff726-32c0-461f-addf-369cd4a4a3b7) uuid!"))


if __name__ == '__main__':
    unittest.main()
