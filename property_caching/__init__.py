from functools import update_wrapper


_CLASS_CACHE_ATTR_NAME = '_class_cached_properties'
_OBJ_CACHE_ATTR_NAME = '_cached_properties'


def class_cached_property(fn):
    def _class_cached_property(self):
        return _get_property_value(fn, self.__class__, _CLASS_CACHE_ATTR_NAME)
    return property(update_wrapper(_class_cached_property, fn))


def cached_property(fn):
    def _cached_property(self):
        return _get_property_value(fn, self, _OBJ_CACHE_ATTR_NAME)
    return property(update_wrapper(_cached_property, fn))


def truthy_cached_property(fn):
    def _truthy_cached_property(self):
        return _get_property_value(
            fn, self, _OBJ_CACHE_ATTR_NAME, cache_false_results=False)
    return property(update_wrapper(_truthy_cached_property, fn))


def set_property_cache(obj, name, value):
    cache = _get_cache(obj)
    cache[name] = value
    setattr(obj, _OBJ_CACHE_ATTR_NAME, cache)


def clear_property_cache(obj, name):
    cache = _get_cache(obj)
    if name in cache:
        del cache[name]


def is_property_cached(obj, name):
    cache = _get_cache(obj)
    return name in cache


def _get_cache(obj, cache_attr_name=_OBJ_CACHE_ATTR_NAME):
    return getattr(obj, cache_attr_name, {})


def _get_property_value(fn, obj, cache_attr_name, cache_false_results=True):
    result = None
    cache = _get_cache(obj, cache_attr_name)
    if fn.__name__ not in cache:
        result = fn(obj)
        # re-read cache since it might be already populated by nested functions
        cache = _get_cache(obj, cache_attr_name)
        if result or cache_false_results:
            cache[fn.__name__] = result
        setattr(obj, cache_attr_name, cache)
    return cache.get(fn.__name__, result)
