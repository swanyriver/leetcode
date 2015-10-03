class node(object):
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.sentinal = node(None)
        self.sentinal.next = self.sentinal.prev = self.sentinal

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache: return -1
        
        accessNode = self.cache[key][1]

        #remove node from que
        accessNode.prev.next = accessNode.next
        accessNode.next.prev = accessNode.prev    
        #move key to back of que
        accessNode.next = self.sentinal.next
        self.sentinal.next = accessNode
        accessNode.next.prev = accessNode
        accessNode.prev = self.sentinal
        
        return self.cache[key][0]
        
    def set(self, key, value):
        
        if key in self.cache:
            accessNode = self.cache[key][1]

            #remove node from que
            accessNode.prev.next = accessNode.next
            accessNode.next.prev = accessNode.prev    
        else:
            accessNode = node(key)

        self.cache[key] = (value,accessNode)

        #move key to back of que
        accessNode.next = self.sentinal.next
        self.sentinal.next = accessNode
        accessNode.next.prev = accessNode
        accessNode.prev = self.sentinal
            
        
        if len(self.cache) == self.capacity:
            self.set = self.setatCapacity

    def setatCapacity(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.cache:
            accessNode = self.cache[key][1]

            #remove node from que
            accessNode.prev.next = accessNode.next
            accessNode.next.prev = accessNode.prev

        else:
            #delete last key from que and from cache
            self.cache.pop(self.sentinal.prev.key,None)
            
            delNode = self.sentinal.prev
            delNode.prev.next = delNode.next
            delNode.next.prev = delNode.prev

            accessNode = node(key)


        self.cache[key] = (value,accessNode)

        #move key to back of que
        accessNode.next = self.sentinal.next
        self.sentinal.next = accessNode
        accessNode.next.prev = accessNode
        accessNode.prev = self.sentinal

        
        

c = LRUCache(3)
s = []
c.set(1,1)
c.set(2,2)
c.set(3,3)
c.set(4,4)
s.append(c.get(4))
s.append(c.get(3))
s.append(c.get(2))
s.append(c.get(1))
c.set(5,5)
s.append(c.get(1))
s.append(c.get(2))
s.append(c.get(3))
s.append(c.get(4))
s.append(c.get(5))

print s