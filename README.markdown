# Property caching

Cached version of property

Written and used by the folks at Yola. Check out our [free website][1] builder today.

## Overview

- cached_property - stores results of decorated functions in decorated object
(in _cached_properties attribute)
- clear_cached_properties_for - deletes cached value(s)

## Usage
    from property_caching.decorators import (cached_property, clear_cached_properties_for)

    class Dummy:
        @cached_property
        def foo(self):
            return 5

        @cached_property
        def bar(self):
            return 42

    d = Dummy()
    d.foo   # calculates result and stores it in d._cached_properties
    d.foo   # uses cached value

    clear_cached_properties_for(d, 'foo')  # clears cache for property `foo`
    clear_cached_properties_for(d)         # clears cache for all properties

## Testing

Install development requirements:

    pip install -r requirements.txt

Run the tests with:

    nosetests

[1]:https://www.yola.com/