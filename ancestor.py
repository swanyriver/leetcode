# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inTree(t,v):
    s = [t]
    while s:
        visit = s.pop()
        if visit is v: return True
        if visit.left: s.append(visit.left)
        if visit.right: s.append(visit.right)

    return False

def pathToValue(t,p,q, path):
    
    if not t: return False

    if t is p:
        path.append(t)
        return q
    if t is q:
        path.append(t)
        return p

    search = pathToValue(t.left,p,q,path) or pathToValue(t.right,p,q,path)
    if search:
        path.append(t)
        return search
    return False


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        path = []
        other = pathToValue(root,p,q,path)

        #path.reverse()

        print path, other

        if inTree(path[0],other): return path[0]
        #path.pop()

        #print inTree(t,other)

        #while path:
            # print path
            # n = path.pop()
            # print "n:",n
            # print n.right and True
        for n in path[1:]:
            print n
            if n.right and inTree(n.right,other): return n
            

import treetrav

t = treetrav.makeTree(range(20),0)
p = t.right.left
q = t.right.right.left

print p,q

x = Solution()
l = x.lowestCommonAncestor(t,p,q)
print "lowest is:", l

 