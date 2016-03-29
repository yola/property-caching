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


def _update_cache(obj, cache_attr_name, cache_key, result):
    cache = _get_cache(obj, cache_attr_name)
    cache[cache_key] = result
    setattr(obj, cache_attr_name, cache)


def _get_property_value(fn, obj, cache_attr_name, cache_false_results=True):
    cache = _get_cache(obj, cache_attr_name)
    cache_key = fn.__name__

    if cache_key in cache:
        return cache[fn.__name__]

    result = fn(obj)
    if result or cache_false_results:
        _update_cache(obj, cache_attr_name, cache_key, result)

    return result
