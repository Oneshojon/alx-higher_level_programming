#!/usr/bin/python3
"""
A test class for a function
"""


import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.asserTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = "Hello world"
        self.assertEqual(s.split(), ["Hello", "world"])
        # check that s.split fails when the seperator is not a string
        with self.assertRaises(TypeError):
            s.split(5)


if __name__ = '__main__':
    unittest.main()
