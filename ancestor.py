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

def pathto(t,p,q):
    s = []
    current = t

    while s or current:
        if current:

            if current is p:
                return q,s,p
            if current is q:
                return p,s,q

            s.append(current)
            current = current.left
        else:
            current = s.pop()
            
            if current is p:
                return q,s,p
            if current is q:
                return p,s,q

            current = current.right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p is root or q is root: return root
        
        other,path,self = pathto(root,p,q)

        print other,path,self


        if inTree(self,other): return self

        for n in path[::-1]:
            if n.right and inTree(n.right,other): return n
            

import treetrav

t = treetrav.makeTree(range(20),0)
#p = t.left.left
#q = t.right.right.left
p = t.left.left
q = p.left

print p,q


# t = treetrav.makeTree([1,2],0)
# p = t
# q = t.right


x = Solution()
l = x.lowestCommonAncestor(t,p,q)
print "lowest is:", l

 