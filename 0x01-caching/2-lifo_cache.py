#!/usr/bin/python
"""
LIFOCache class that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize and inherit self.cache_data from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        Args:
            key: key to be added to the dictionary self.cache_data
            item: the value for the key
        If key or item is None, the method does nothing
        If number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS, the first item put in cache
            must be discarded, then print "DISCARD:" with the key discarded
        """
        if (key is not None and item is not None):
            num_of_items = len(self.cache_data)
            if (num_of_items >= BaseCaching.MAX_ITEMS):
                if (self.cache_data.get(key)):
                    self.cache_data.update({key: item})
                else:
                    last = list(self.cache_data.keys())[-1]
                    self.cache_data.pop(last)
                    print("DISCARD: {}".format(last))
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        Arg:
            key: the key to get the value in self.cache_data
        Return:
            value in self.cache_data linked to key
            If key is None or doesn't exist, return None
        """
        if (key is None or self.cache_data.get(key) is None):
            return None
        return self.cache_data.get(key)
