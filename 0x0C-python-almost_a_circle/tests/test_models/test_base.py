#!/usr/bin/python3
import unittest
"""
Tests for classes in the models package
"""


class TestModels(unittest.TestCase):
    """
    Tests for classes in the models package
    """
    def test_base(self):
        self.assertEqual(self, self)
