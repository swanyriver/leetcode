class node(object):
    """docstring for node"""
    def __init__(self, val, l, r):
        self.val = val
        self.left = l
        self.right = r
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)


def makeTree(l,i=0):
    """ returns node """
    return None if i >= len(l) else node(l[i], makeTree(l,i*2+1) ,makeTree(l,i*2+2) )


def preorder(t):
    s = [t]

    while s:
        visit = s.pop()
        yield visit.val

        if visit.right:s.append(visit.right)
        if visit.left:s.append(visit.left)

def levelorder(t):
    q = [t]

    while q:
        visit = q.pop(0)
        yield visit.val

        if visit.left: q.append(visit.left)
        if visit.right: q.append(visit.right)



def pathToValue(t,val, path):
    
    if not t: return False

    if t.val == val or pathToValue(t.left,val,path) or pathToValue(t.right,val,path):
        path.append(t)
        return True


# void in_order_traversal_iterative(BinaryTree *root) {
#   stack<BinaryTree*> s;
#   BinaryTree *current = root;
#   while (!s.empty() || current) {
#     if (current) {
#       s.push(current);
#       current = current->left;
#     } else {
#       current = s.top();
#       s.pop();
#       cout << current->data << " ";
#       current = current->right;
#     }
#   }
# }

def inorder(t):
    s = []
    current = t

    while s or current:
        if current:
            s.append(current)
            current = current.left
        else:
            current = s.pop()
            yield current
            current = current.right

tree = makeTree(range(20))
