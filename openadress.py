class Tombstone():
    def __init__(self):
        pass

from collections import namedtuple
hasnode = namedtuple('HashNode', ['key', 'value'])


class OAhash(object):
    """docstring for OAhash"""
    def __init__(self,capacity):
        #self.used = 0
        self.map = [None] * capacity
        self.tomb = Tombstone()
    def haskey(self,key):
        return bool(self.get(key))

    def get(self,key):
        indx = self.findIndex(key)
        if indx: return self.map[indx].value
        return None

    def findIndex(self,key):
        hs = hash(key)%len(self.map)

        if self.map[hs] and self.map[hs].key == key: return self.map[hs].value

        search = (hs+1)%len(self.map)

        while search != hs:
            if self.map[search] is None: return None
            if self.map[search] is self.tomb: continue
            if self.map[search] and self.map[search].key == key:
                return search

        return None

    def set(self,key,value):
        hs = hash(key)%len(self.map)

        #stop when map[hs] == none or self
        while self.map[hs] is not None and self.map[hs] is not self.tomb and self.map[hs].key != key: 
            hs = (hs+1)%len(self.map)

        self.map[hs] = hasnode(key,value)

    def delkey(self,key):
        indx = self.findIndex(key)
        if indx: self.map[indx] = self.tomb
        



        