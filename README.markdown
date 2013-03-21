# Property caching

Cached version of property

Written and used by the folks at Yola. Check out our [free website][1] builder today.

## Overview

- cached_property - stores results of decorated functions in decorated object
(in _cached_properties attribute)
- clear_cached_property - deletes cached value

## Usage
    from property_caching.decorators import (cached_property, clear_cached_property)

    class Dummy:
        @cached_property
        def foo(self):
            return expensive_operation()

    d = Dummy()
    d.foo   # calculates result and stores it in d._cached_properties
    d.foo   # uses cached value

    clear_cached_property(d, 'foo')  # clears cache for property `foo`

## Testing

Install development requirements:

    pip install -r requirements.txt

Run the tests with:

    nosetests

[1]:https://www.yola.com/