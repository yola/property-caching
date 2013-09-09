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


def _get_property_value(fn, obj, cache_attr_name):
    cache = _get_cache(obj, cache_attr_name)
    if not fn.__name__ in cache:
        cache[fn.__name__] = fn(obj)
        setattr(obj, cache_attr_name, cache)
    return cache[fn.__name__]
