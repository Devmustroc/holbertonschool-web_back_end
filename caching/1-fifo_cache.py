#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    order = []

    def __int__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.order[0]
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
                    self.order.pop(0)
                self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None