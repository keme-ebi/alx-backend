#!/usr/bin/python
"""
MRUCache class that inherits from BaseCaching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize and inherit self.cache_data from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()

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
                    return
                else:
                    recent, val = self.cache_data.popitem(last=True)
                    print("DISCARD: {}".format(recent))
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
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)