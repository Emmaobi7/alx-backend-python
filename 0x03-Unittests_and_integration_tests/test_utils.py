#!/usr/bin/env python3
"""
test for utils
nested_maps
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, x, y, exp):
        """
        test access nested method
        correct out put
        """
        res = access_nested_map(x, y)
        self.assertEqual(res, exp)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, x, y):
        """
        raise error exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(x, y)


class TestGetJson(unittest.TestCase):
    """
    tests for get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, x, exp):
        """
        test get request made just once
        test for output
        """
        with unittest.mock.patch('utils.requests.get',
                                 return_value=Mock(json=lambda: exp)) as m_get:
            res = get_json(x)
            m_get.assert_called_once_with(x)
            self.assertEqual(res, exp)


class TestMemoize(unittest.TestCase):
    """
    tests for memoize decorator
    """
    def test_memoize(self):
        """
        call a a_property twice
        calla a_method once
        """
        class TestClass:
            """
            memoize test class
            """
            def a_method(self):
                """
                return integer
                42
                """
                return 42

            @memoize
            def a_property(self):
                """
                return a.method
                """
                return self.a_method()
        with unittest.mock.patch.object(TestClass, 'a_method') as mthd:
            test_ins = TestClass()
            res1 = test_ins.a_property()
            res2 = test_ins.a_property()
            self.assertEqual(res1, res2)
            mthd.assert_called_once()


if __name__ == '__main__':
    unittest.main()
