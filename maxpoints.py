

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return "(%d,%d)"%(self.x,self.y)
    def __repr__(self): 
        return "(%d,%d)"%(self.x,self.y)

from collections import defaultdict
from itertools import combinations
from fractions import gcd

x = 0
y = 1

def pointWalk(pointa,pointb):
    difx = pointb[x]-pointa[x]
    dify = pointb[y]-pointa[y]

    simplifiy = abs(gcd(difx,dify))
    dify /= simplifiy
    difx /= simplifiy

    while pointa != pointb:
        yield pointa
        pointa = (pointa[x] + difx, pointa[y] + dify)
    yield pointb




class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        if len(points) < 3: return len(points)
        
        dpoints = defaultdict(int)
        for p in points: dpoints[(p.x,p.y)] += 1
        points = set([ (p.x,p.y) for p in points])

        maximum = max(dpoints.values())

        for pointpair in combinations(points,2):
            line = 0
            for p in pointWalk(*pointpair): 
                line+=dpoints[p]
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

points = [Point(2,3),Point(3,3),Point(-5,3)]

#points = list(set(points))

##print points

print s.maxPoints(points)


#############################################
##### 104 ms ################################
##no itertools, but in is run on set ########
#############################################
#from itertools import combinations

# def gcd(u, v):
#     while v:
#         u, v = v, u % v
#     return abs(u)

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             if (p.x,p.y) in dpoints: 
#                 dpoints[(p.x,p.y)] += 1
#             else:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = set([ (p.x,p.y) for p in points])
#         Lpoints = list(points)

#         maximum = max(dpoints.values())

#         #for pointpair in combinations(points,2):
#         for i in range(len(points)):
#             for j in range(i+1,len(points)):
#                 line = 0
#                 for p in pointWalk(Lpoints[i],Lpoints[j]): 
#                     if p in dpoints:line+=dpoints[p]
#                 if line > maximum: maximum = line

#         return maximum




#############################################
############ 120 ms #########################
###list isntead of set and no itertools######
#############################################
# #from itertools import combinations

# def gcd(u, v):
#     while v:
#         u, v = v, u % v
#     return abs(u)

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             if (p.x,p.y) in dpoints: 
#                 dpoints[(p.x,p.y)] += 1
#             else:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = list(set([ (p.x,p.y) for p in points]))

#         maximum = max(dpoints.values())

#         #for pointpair in combinations(points,2):
#         for i in range(len(points)):
#             for j in range(i+1,len(points)):
#                 line = 0
#                 for p in pointWalk(points[i],points[j]): 
#                     if p in dpoints:line+=dpoints[p]
#                 if line > maximum: maximum = line

#         return maximum




##################################################
######   112ms ##################################
###use iterative gcd algorithm #################
################################################
# from itertools import combinations

# def gcd(u, v):
#     while v:
#         u, v = v, u % v
#     return abs(u)

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             if (p.x,p.y) in dpoints: 
#                 dpoints[(p.x,p.y)] += 1
#             else:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = set([ (p.x,p.y) for p in points])

#         maximum = max(dpoints.values())

#         for pointpair in combinations(points,2):
#             line = 0
#             for p in pointWalk(*pointpair): 
#                 if p in dpoints:line+=dpoints[p]
#             if line > maximum: maximum = line

#         return maximum

#############################################
########Runtime: 116 ms######################
###without generator, exactly the same#######
#############################################

# from itertools import combinations
# from fractions import gcd

# x = 0
# y = 1

# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             if (p.x,p.y) in dpoints: 
#                 dpoints[(p.x,p.y)] += 1
#             else:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = set([ (p.x,p.y) for p in points])

#         maximum = max(dpoints.values())

#         for point in combinations(points,2):
#             line = 0

#             ###############################################
#             pointa, pointb = point[0],point[1]
#             difx = pointb[x]-pointa[x]
#             dify = pointb[y]-pointa[y]
        
#             simplifiy = abs(gcd(difx,dify))
#             dify /= simplifiy
#             difx /= simplifiy
        
#             while pointa != pointb:
#                 if pointa in dpoints:line+=dpoints[pointa]
#                 pointa = (pointa[x] + difx, pointa[y] + dify)

#             line+=dpoints[point[1]]
            
#             ###############################################
            
#             if line > maximum: maximum = line

#         return maximum

#############################################
########Runtime: 116 ms######################
####if in else for dict instead of default###
#############################################

# from itertools import combinations
# from fractions import gcd

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             if (p.x,p.y) in dpoints: 
#                 dpoints[(p.x,p.y)] += 1
#             else:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = set([ (p.x,p.y) for p in points])

#         maximum = max(dpoints.values())

#         for pointpair in combinations(points,2):
#             line = 0
#             for p in pointWalk(*pointpair): 
#                 if p in dpoints:line+=dpoints[p]
#             if line > maximum: maximum = line

#         return maximum


#####################################
##########  180ms ###################
##using try except instead of ddict##
#####################################
# from itertools import combinations
# from fractions import gcd

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = {}
#         for p in points:
#             try: 
#                 dpoints[(p.x,p.y)] += 1
#             except KeyError:
#                 dpoints[(p.x,p.y)] = 1
                
#         points = set([ (p.x,p.y) for p in points])

#         maximum = max(dpoints.values())

#         for pointpair in combinations(points,2):
#             line = 0
#             for p in pointWalk(*pointpair): 
#                 try:line+=dpoints[p]
#                 except KeyError: pass
#             if line > maximum: maximum = line

#         return maximum


#####################################
##########  152ms ###################
#####################################
# from collections import defaultdict
# from itertools import combinations
# from fractions import gcd

# x = 0
# y = 1

# def pointWalk(pointa,pointb):
#     difx = pointb[x]-pointa[x]
#     dify = pointb[y]-pointa[y]

#     simplifiy = abs(gcd(difx,dify))
#     dify /= simplifiy
#     difx /= simplifiy

#     while pointa != pointb:
#         yield pointa
#         pointa = (pointa[x] + difx, pointa[y] + dify)
#     yield pointb




# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """

#         if len(points) < 3: return len(points)
        
#         dpoints = defaultdict(int)
#         for p in points: dpoints[(p.x,p.y)] += 1
#         points = set([ (p.x,p.y) for p in points])

#         maximum = max(dpoints.values())

#         for pointpair in combinations(points,2):
#             line = 0
#             for p in pointWalk(*pointpair): 
#                 line+=dpoints[p]
#             if line > maximum: maximum = line

#         return maximum
