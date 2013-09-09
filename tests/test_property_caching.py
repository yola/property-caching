import unittest2
from property_caching import *


class TestClass(object):
    counter3 = 0

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

    @class_cached_property
    def method3(self):
        self.counter3 += 1
        return self.counter3


class BaseTestCase(unittest2.TestCase):
    def setUp(self):
        self.test_obj = TestClass()


class CachedPropertyTestCase(BaseTestCase):
    """A method decorated with @cached_property"""

    def test_returns_the_calculated_value(self):
        self.assertEqual(self.test_obj.counter, 0)
        self.assertEqual(self.test_obj.method, 1)

    def test_does_not_recalculate_the_value_on_subsequent_calls(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.counter, 1)


class ClassCachedPropertyTestCase(BaseTestCase):
    """A method decorated with @class_cached_property"""

    def test_does_not_recalculate_the_value_on_subsequent_calls(self):
        self.assertEqual(self.test_obj.method3, 1)
        self.assertEqual(self.test_obj.method3, 1)
        self.assertEqual(TestClass.counter3, 1)

    def test_shares_cached_property_among_all_objects_of_the_class(self):
        obj1 = TestClass()
        self.assertEqual(obj1.method3, 1)
        obj2 = TestClass()
        self.assertEqual(obj2.method3, 1)
        self.assertEqual(TestClass.counter3, 1)


class ClearPropertyCacheTestCase(BaseTestCase):
    """clear_property_cache(object, property_name)"""

    def test_clears_the_calculated_value(self):
        self.assertEqual(self.test_obj.method, 1)
        clear_property_cache(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)

    def test_does_not_affect_other_cached_properties_on_the_object(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertEqual(self.test_obj.method2, 1)
        clear_property_cache(self.test_obj, 'method')
        self.assertEqual(self.test_obj.method, 2)
        self.assertEqual(self.test_obj.method2, 1)


class SetPropertyCacheTestCase(BaseTestCase):
    """set_property_cache(object, property_name, property_value)"""

    def test_sets_cache_for_the_given_property_name(self):
        self.assertEqual(self.test_obj.method, 1)
        set_property_cache(self.test_obj, 'method', 10)
        self.assertEqual(self.test_obj.method, 10)


class IsPropertyCachedTestCase(BaseTestCase):
    """is_property_cached(object, property_name)"""

    def test_returns_true_if_property_is_cached(self):
        self.assertEqual(self.test_obj.method, 1)
        self.assertTrue(is_property_cached(self.test_obj, 'method'))

    def test_returns_false_if_property_is_not_cached(self):
        self.assertFalse(is_property_cached(self.test_obj, 'method'))
