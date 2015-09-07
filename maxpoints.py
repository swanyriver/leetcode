

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return "(%d,%d)"%(self.x,self.y)
    def __repr__(self): 
        return "(%d,%d)"%(self.x,self.y)

from collections import Counter
from collections import defaultdict
from itertools import combinations
from fractions import gcd

x = 0
y = 1

def pointWalk(pointa,pointb):
    difx = pointb[x]-pointa[x]
    dify = pointb[y]-pointa[y]

    if not difx:
        for ycord in range(min(pointa[y],pointb[y])+1, max( pointa[y],pointb[y])):
            yield (pointa[x],ycord)
        return

    if not dify:
        for xcord in range(min(pointa[x],pointb[x])+1, max( pointa[x],pointb[x])):
            yield (xcord,pointa[y])
        return

    simplifiy = abs(gcd(difx,dify))
    dify /= simplifiy
    difx /= simplifiy

    print pointa , "--->", pointb, "%d/%d"%(difx,dify)
    pointa = (pointa[x] + difx, pointa[y] + dify)

    while pointa != pointb:
        print pointa
        raw_input()
        yield pointa
        pointa = (pointa[x] + difx, pointa[y] + dify)




class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        points = set([ (p.x,p.y) for p in points])

        maximum = 2

        for pointpair in combinations(points,2):
            line = 2
            for p in pointWalk(*pointpair): 
                if p in points: line+=1
            if line > maximum: maximum = line

        return maximum
        


s = Solution()

points = [
        Point(2,4),
        Point(2,4),
        Point(2,4),
        Point(2,4),
        Point(2,4),
        Point(2,4),
        Point(2,2),
        Point(1,3),
        Point(1,4),
        Point(6,7),
        Point(6,6),
        Point(6,3),
]

#points = list(set(points))

#print points

print s.maxPoints(points)