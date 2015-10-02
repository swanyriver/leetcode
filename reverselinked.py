class Node(object):
    """docstring for node"""
    def __init__(self, arg):
        self.val = arg
        self.next = None

a = range(1,10)

head = Node(0)
node = head

for x in a:
    node.next = Node(x)
    node = node.next

node = head
while(node):
    print node.val, '->',
    node = node.next

newlist = None
node = head

while node:
    tmp = node.next
    node.next = newlist
    newlist = node
    node = tmp


print ' '
node = newlist
while(node):
    print node.val, '->',
    node = node.next
        