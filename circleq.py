class node(object):
    """docstring for node"""
    def __init__(self, val, mnext):
        self.val = val
        self.next = mnext
        
class circle(object):
    """docstring for circl"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.put = self.putunder

    def putunder(self,v):
        if not self.head
        