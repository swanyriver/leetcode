class Node(object):
    """docstring for node"""
    def __init__(self, arg):
        self.val = arg
        self.next = None

a = range(1,9)

head = Node(0)
node = head

for x in a:
    node.next = Node(x)
    node = node.next

node = head
while(node):
    print node.val, '->',
    node = node.next

s = head
f = head
while(f):
    s = s.next
    f = f.next
    if f: f = f.next


newlist = None
node = s

while node:
    tmp = node.next
    node.next = newlist
    newlist = node
    node = tmp


print ' '
node = head
while(node):
    print node.val, '->',
    node = node.next
        
print ' '
node = newlist
while(node):
    print node.val, '->',
    node = node.next
        