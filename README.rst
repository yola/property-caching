Property caching
================
.. image:: https://travis-ci.org/yola/property-caching.svg?branch=fix/md-to-rst
    :target: https://travis-ci.org/yola/property-caching


Cached version of property

Written and used by the folks at Yola to support our `free website
builder`_.

Overview
--------

-  ``cached_property`` - stores results of decorated methods in
   decorated object
   (in ``_cached_properties`` attribute)
-  ``class_cached_property`` - stores results of decorated methods in
   the class of decorated object
   (in ``_class_cached_properties`` attribute). All instances will share
   cached value.
-  ``clear_property_cache`` - deletes cached value (works for object
   cached properties only)
-  ``set_property_cache`` - explicitly sets property cache (works for
   object cached properties only)
-  ``is_property_cached`` - allows to check whether property was cached
   or not (works for object cached properties only)

Usage
-----

.. code:: python

    from property_caching import (cached_property,
                                  class_cached_property,
                                  clear_property_cache,
                                  set_property_cache,
                                  truthy_cached_property)

    class Dummy:
        @cached_property
        def foo(self):
            return self.service.expensive_operation()

        @truthy_cached_property
        def bar(self):
            # this value will only be cached if it doesn't evaluate to false:
            return self.service.expensive_operation2()

        @class_cached_property
        def service(self):
            return expensive_service_initialization()

    d = Dummy()
    d.foo   # calculates result and stores it in d._cached_properties
    d.foo   # uses cached value

    clear_property_cache(d, 'foo')   # clears cache for property `foo`
    set_property_cache(d, 'foo', 42) # explicitly set cache for property `foo`

    d2 = Dummy()
    d2.foo  # re-calculates value of `foo` but uses cached service

Testing
-------

Install development requirements:

::

    pip install -r requirements.txt

Run the tests with:

::

    python setup.py test

.. _free website builder: https://www.yola.com/

.. image:: https://travis-ci.org/yola/property-caching.svg?branch=fix/md-to-rst
    :target: https://travis-ci.org/yola/property-caching
