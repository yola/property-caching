import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../property_caching')))

import unittest2
from property_caching.decorators import cached_property, clear_cached_properties_for


class TestClass(object):
    def __init__(self):
        self.counter = 0
        self.counter2 = 0

    @cached_property
    def method(self):
        self.counter += 1
        return self.counter

    @cached_property
    def method2(self):
        self.counter2 += 1
        return self.counter2


class DecoratorsTestCase(unittest2.TestCase):
    def setUp(self):
        self.test_obj = TestClass()

    def test_property_caching(self):
        self.assertEqual(self.test_obj.counter, 0)

        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method, 1)

    def test_clearing_cache_for_single_property(self):
        self.assertEqual(self.test_obj.method, 1)
        clear_cached_properties_for(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)

    def test_clearing_cache_for_single_property_does_not_affect_others(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method2, 1)
        clear_cached_properties_for(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)
        self.assertEqual(self.test_obj.method2, 1)

    def test_clearing_cache_for_all_properties(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method2, 1)
        clear_cached_properties_for(self.test_obj)
        self.assertEqual(self.test_obj.method, 2)
        self.assertEqual(self.test_obj.method2, 2)
