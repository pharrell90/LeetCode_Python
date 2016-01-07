'''
 Design and implement a data structure for Least Recently Used (LRU) cache.
 It should support the following operations: get and set.

 get(key) - Get the value (will always be positive) of the key if the key
 exists in the cache, otherwise return -1.

 set(key, value) - Set or insert the value if the key is not already present.
 When the cache reached its capacity, it should invalidate the least recently
 used item before inserting a new item.

 use OrderedDict ot remember the insertion order
 runtime: 336ms
'''

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        '''
        |Input|
          @type capacity: int
          @param capacity:
        |Output|
        '''
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        '''
        |Input|
          @type key:
          @param key:
        |Output|
          @type return: int
        '''
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        '''
        |Input|
          @type key: int
          @type value: int
        |Output|
          @type return: nothing
        '''
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    s = LRUCache(5)

