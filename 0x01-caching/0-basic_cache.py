#!/usr/bin/python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache class
    """
    def __init__(self):
        """
        Initialize and call inherit from the super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        Args:
            key(str): key to add to the dictionary
            item: value for the key
        If key or item is None, the method does nothing
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        Arg:
            key: the key to get the value from
        Return:
            self.cache_data linked to key
            If key is None or the key doesn't exist, return None
        """
        if (key is None or self.cache_data.get(key) == None):
            return None
        return self.cache_data.get(key)
