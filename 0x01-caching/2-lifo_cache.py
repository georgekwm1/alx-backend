#!/usr/bin/python3
"""BasicCache module"""
from BaseCaching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}\n")
                # print(f"DISCARD: {new_dict}\n")
                # count = BaseCaching.MAX_ITEMS + 1
                # for i, (ky, val) in enumerate(new_dict.items()):
                #     count = count - 1
                #     if i == BaseCaching.MAX_ITEMS:
                #         del self.cache_data[ky]
                #         print(f"DISCARD: {ky}\n")
                #         break

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
