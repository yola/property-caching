# Property caching

Cached version of property

Written and used by the folks at Yola. Check out our [free website][1] builder today.

## Overview

- cached_property - stores results of decorated methods in decorated object
(in _cached_properties attribute)
- cached_in_class_property - stores results of decorated methods in the class of decorated object
(in _cached_in_class_properties attribute). All instances will share cached value.
- clear_property_cache - deletes cached value (works for object cached properties only)
- set_property_cache - explicitly sets property cache (works for object cached properties only)

## Usage
    from property_caching.decorators import (cached_property,
                                             cached_in_class_property,
                                             clear_property_cache,
                                             set_property_cache)

    class Dummy:
        @cached_property
        def foo(self):
            return service.expensive_operation()

        @cached_in_class_property
        def service(self):
            return expensive_service_initialization()

    d = Dummy()
    d.foo   # calculates result and stores it in d._cached_properties
    d.foo   # uses cached value

    clear_property_cache(d, 'foo')   # clears cache for property `foo`
    set_property_cache(d, 'foo', 42) # implicitly set cache for property `foo`

    d2 = Dummy()
    d2.foo  # re-calculates value of `foo` but uses cached service


## Testing

Install development requirements:

    pip install -r requirements.txt

Run the tests with:

    nosetests

[1]:https://www.yola.com/