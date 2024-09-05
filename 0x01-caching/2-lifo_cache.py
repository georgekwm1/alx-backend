#!/usr/bin/python3
"""BasicCache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    # def put(self, key, item):
    #     """Add an item in the cache"""
    #     if key is not None and item is not None:
    #         if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
    #             keys = list(self.cache_data.keys())
    #             last_key = keys[-1]
    #             first_key = next(iter(self.cache_data))
    #             self.cache_data.pop(last_key)
    #             print(f"DISCARD: {last_key}\n")
    #     self.cache_data[key] = item
    #     self.cache_data.move_to_end(key, last=True)
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
