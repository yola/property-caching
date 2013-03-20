import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../property_caching')))

import unittest2
from property_caching.decorators import cached_property, clear_cached_property


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


class BaseTestCase(unittest2.TestCase):
    def setUp(self):
        self.test_obj = TestClass()


class DecoratorTestCase(BaseTestCase):
    """A method decorated with @cached_property"""

    def test_returns_the_calculated_value(self):
        self.assertEqual(self.test_obj.counter, 0)
        self.assertEqual(self.test_obj.method, 1)

    def test_does_not_recalculate_the_value_on_subsequent_calls(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method, 1)


class ClearCachedPropertyTestCase(BaseTestCase):
    """clear_cached_property(object, method_name)"""

    def test_clears_the_calculated_value(self):
        self.assertEqual(self.test_obj.method, 1)
        clear_cached_property(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)

    def test_does_not_affect_other_cached_properties_on_the_object(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method2, 1)
        clear_cached_property(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)
        self.assertEqual(self.test_obj.method2, 1)
