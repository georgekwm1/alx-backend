#!/usr/bin/python3
"""BasicCache module"""
from BaseCaching import BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            new_dict = self.cache_data
            count = 0
            for ky in new_dict:
                count += 1
                if count == 1:
                    del self.cache_data[ky]
                    print(f"DISCARD: {ky}\n")
                    break

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
