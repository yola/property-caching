from functools import update_wrapper


def cached_property(fn):
    def cached_property(self):
        cache = getattr(self, '_cached_properties', {})
        self._cached_properties = cache
        return cache.setdefault(fn.__name__, fn(self))
    return property(update_wrapper(cached_property, fn))


def clear_cached_property(obj, method_name):
    cache = getattr(obj, '_cached_properties', {})
    if method_name in cache:
        del cache[method_name]
