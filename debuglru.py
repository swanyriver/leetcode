class node(object):
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

def pSent(node):
    n2 = node.next
    while n2 is not node:
        print n2.key, '->',
        n2 = n2.next

    print ''

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.sentinal = node(None)
        self.sentinal.next = self.sentinal
        self.sentinal.prev = self.sentinal

    def get(self, key):
        """
        :rtype: int
        """

        print "get %d, cache:%r, que:"%(key,self.cache.keys()),
        pSent(self.sentinal)

        if key not in self.cache: 
            print "not in there"
            print "---------------------------------------------"
            return -1
        
        accessNode = self.cache[key][1]

        #remove node from que
        accessNode.prev.next = accessNode.next
        accessNode.next.prev = accessNode.prev    
        #move key to back of que
        accessNode.next = self.sentinal.next
        self.sentinal.next = accessNode
        accessNode.next.prev = accessNode
        accessNode.prev = self.sentinal

        print "after: cache:%r, que:"%(self.cache.keys()),
        pSent(self.sentinal)
        print "----------------------------------------"
        
        return self.cache[key][0]
        
    # def set(self,key,value):
        
    #     lnode = node(key)
        
    #     self.cache[key] = (value,lnode)
        
    #     self.sentinal.next = self.sentinal.prev = lnode
    #     lnode.prev = lnode.next = self.sentinal
        
    #     self.set = self.settoCapacity if self.capacity > 1 else self.setatCapacity
        
        
    def set(self, key, value):

        print "set to cap: %d, cache:%r, que:"%(key,self.cache.keys()),
        pSent(self.sentinal)

        
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
            
        print "after, cache:%r, que:"%(self.cache.keys()),
        pSent(self.sentinal)
        print "--------------------------------------------------------"
        
        if len(self.cache) == self.capacity:
            self.set = self.setatCapacity

    def setatCapacity(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        print "set @ cap: %d, cache:%r, que:"%(key,self.cache.keys()),
        pSent(self.sentinal)
        print "sentinal prev = ", self.sentinal.prev.key

        if key in self.cache:
            accessNode = self.cache[key][1]

            #remove node from que
            accessNode.prev.next = accessNode.next
            accessNode.next.prev = accessNode.prev

        else:
            #delete last key from que and from cache
            self.cache.pop(self.sentinal.prev.key,None)
            #self.sentinal.prev = self.sentinal.prev.prev

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

        print "after, cache:%r, que:"%(self.cache.keys()),
        pSent(self.sentinal)
        print "--------------------------------------------------------"

        
        

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