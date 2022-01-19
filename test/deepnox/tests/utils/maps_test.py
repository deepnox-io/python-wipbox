import unittest

from deepnox.helpers.testing_helpers import BaseTestCase
from deepnox.utils.maps import (
    Map,
    UpperMap,
    CannotConvertToMapTypeError,
    to_map,
)


class MapTestCase(BaseTestCase):
    def test___init__(self):
        self.assertIsInstance(Map(), Map)
        m = Map(name="name_test", value="value_test")
        self.assertIsInstance(m, Map)
        self.assertEqual(m["name"], "name_test")
        self.assertEqual(m["value"], "value_test")

    def test___init___passing_a_dict_as_parameter(self):
        self.assertIsInstance(
            Map({"name": "name_test", "value": "value_test"}), Map
        )
        m = Map(name="name_test", value="value_test")
        self.assertIsInstance(m, Map)
        self.assertEqual(m["name"], "name_test")
        self.assertEqual(m["value"], "value_test")

    def test_delete_attribute_should_not_raise_an_exception(self):
        m = Map({"name": "value"})
        self.assertNotRaises(Exception, lambda: delattr(m, "name"))

    def test_delete_key_should_not_raise_an_exception(self):
        m = Map({"name": "value"})
        self.assertNotRaises(Exception, lambda: m["name"])


class UpperMapTestCase(unittest.TestCase):
    def test_create_uppermap_with_named_param(self):
        self.assertIsInstance(UpperMap(), UpperMap)
        m = UpperMap(name="name_test", value="value_test")
        self.assertIsInstance(m, UpperMap)
        self.assertEqual(m["name"], "name_test")
        self.assertEqual(m["value"], "value_test")
        self.assertEqual(m.name, "name_test")
        self.assertEqual(m.value, "value_test")
        self.assertEqual(m.NAME, "name_test")
        self.assertEqual(m.VALUE, "value_test")

    def test_create_uppermap_with_dict_param(self):
        d = {
            "service": {
                "image": "image_test",
                "tag": "tag_test",
            }
        }
        self.assertIsInstance(UpperMap(d), UpperMap)
        m = UpperMap(d)
        self.assertIsInstance(m, UpperMap)
        self.assertEqual(type(m.get("service")), UpperMap)
        self.assertEqual(m.get("service").get("image"), "image_test")
        self.assertEqual(m.SERVICE.IMAGE, "image_test")


class CannotConvertToMapTypeErrorTestCase(unittest.TestCase):
    def test___init__(self):
        """
        :credits: https://stackoverflow.com/a/8294654
        """
        self.assertIsInstance(
            CannotConvertToMapTypeError(param="param_name_test"),
            CannotConvertToMapTypeError,
        )
        self.assertRaises(
            CannotConvertToMapTypeError,
            lambda: (_ for _ in ()).throw(
                CannotConvertToMapTypeError(param="param_name_test")
            ),
        )


class FunctionToMapTestCase(unittest.TestCase):
    def test_should_returns_an_empty_card_if_no_parameters_are_passed(self):
        m = Map()
        self.assertIsInstance(m, Map)
        self.assertEqual(m.test, None)

    def test_should_returns_an_empty_card_if_a_dictionary_is_passed_in_parameter(
        self,
    ):
        m = Map({"name": "name_test", "value": "value_test"})
        self.assertIsInstance(m, Map)
        self.assertEqual("name_test", m.name)
        self.assertEqual("value_test", m.value)

    def test_should_returns_an_empty_card_if_a_dictionary_is_a_string_is_passed_in_parameter(
        self,
    ):
        self.assertRaises(
            CannotConvertToMapTypeError, lambda: Map("an_unreadable_string")
        )

    def test_should_returns_an_empty_map_if_missing_positional_argument(self):
        self.assertIsInstance(to_map(), Map)
        self.assertEqual(len(to_map().keys()), 0)

    def test_calling_to_map_using_a_map_as_argument_should_return_the_same_map(
        self,
    ):
        o = Map({"name": "name_test"})
        self.assertEqual(o, to_map(o))
        self.assertEqual(id(o), id(to_map(o)))
        self.assertEqual(o.name, to_map(o).name)

    def test_calling_to_map_using_invalid_poisitional_argument_should_raise_an_error(
        self,
    ):
        self.assertRaises(CannotConvertToMapTypeError, lambda: to_map("test"))


if __name__ == "__main__":
    unittest.main()
