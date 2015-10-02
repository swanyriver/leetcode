from heapq import *

import functools
@functools.total_ordering
class path(object):
    def __init__(self, chealth, shealth, x, y):
        self.chealth = chealth
        self.shealth = shealth
        self.x = x
        self.y = y
        
    def __eq__(self,other):
        return self.shealth == other.shealth
    def __lt__(self,other):
        return self.shealth < other.shealth
        

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon[0][0] < 0: start = abs(dungeon[0][0]) + 1
        else: start = 1
        
        pathPQ = [  ]
        
        nextPath = path( start+dungeon[0][0], start, 0,0,)
        
        Px = len(dungeon[0]) - 1
        Py = len(dungeon) - 1

        reached = set()

        print "princess @%d,%d"%(Px,Py)
        
        
        while nextPath.y != Py or nextPath.x != Px:
            #if (nextPath.x,nextPath.y) in reached:pass
            #reached.add((nextPath.x,nextPath.y))
            
            #print "Knight @%d,%d  "%(nextPath.x,nextPath.y), "princess @%d,%d"%(Px,Py)
            
            #add right
            #if nextPath.x < Px and (nextPath.x+1,nextPath.y) not in reached:
            if nextPath.x < Px:
                right = dungeon[nextPath.y][nextPath.x+1]
                if right < 0 and nextPath.chealth <= abs(right):
                    heappush( pathPQ, path(chealth=1,shealth= nextPath.shealth + abs(nextPath.chealth+right) + 1
                        ,x=nextPath.x+1,y=nextPath.y) )
                else:
                    heappush( pathPQ, path(chealth= nextPath.chealth + right,shealth= nextPath.shealth
                        ,x=nextPath.x+1,y=nextPath.y) )
            
            
            
            #add down
            #if nextPath.y < Py and (nextPath.x+1,nextPath.y) not in reached:
            if nextPath.y < Py:
                down = dungeon[nextPath.y+1][nextPath.x]
                if down < 0 and nextPath.chealth <= abs(down):
                    heappush( pathPQ, path(chealth=1,shealth= nextPath.shealth + abs(nextPath.chealth+down) + 1
                        ,x=nextPath.x,y=nextPath.y+1) )
                else:
                    heappush( pathPQ, path(chealth= nextPath.chealth + down,shealth= nextPath.shealth
                        ,x=nextPath.x,y=nextPath.y+1) )
            
            
            nextPath = heappop(pathPQ)
        
        return nextPath.shealth
        
        
        

dungeon = [[29,-78,-52,-1,-38,6,24,-45,35,-29],[-48,-48,-52,2,-96,-78,-96,40,-78,-73],[-31,-73,-19,38,14,-95,28,-59,29,-20],[17,-86,45,15,-3,-53,43,42,-97,-1],[20,-99,-4,-2,-87,-98,7,-90,-33,-42],[-77,-66,-54,-46,38,-42,3,-5,-45,-49],[13,-13,-52,-63,25,9,-63,-6,-58,-86],[-57,38,-83,41,-71,-18,9,-57,35,-33],[-2,-2,-95,-85,-37,-9,-60,-95,-87,-99],[46,-98,-77,-13,-76,36,-38,-19,-63,5],[-66,-15,-45,-81,-51,6,-29,-96,6,28],[-22,17,34,-52,-14,-65,-17,-70,10,-40],[18,-37,23,-76,-5,4,-31,-59,-22,30],[-26,-12,-34,9,-78,-53,-98,-37,-1,29],[-54,-94,37,-8,22,-16,-84,-100,-45,13],[25,-96,28,-77,5,-93,4,20,-41,-89],[-90,-99,-47,29,14,-47,-78,-40,-56,26],[-82,-69,-56,-40,6,0,-20,5,-39,-73],[-100,44,11,37,43,45,-23,8,16,45],[-33,41,-89,-13,-63,46,17,26,-65,23],[-48,2,-32,-56,-55,-21,-63,-9,-23,-61],[-56,44,-34,45,45,-23,41,9,7,-90],[34,49,-66,-41,37,-56,-62,-71,28,-87],[-54,-36,-78,-37,-22,27,-64,-58,-3,-70],[-77,-23,-60,-99,45,-47,-42,9,-72,-3],[30,29,2,-50,-46,6,-72,0,-39,-4],[32,29,-67,-38,-56,-43,50,-65,-81,-3],[31,-31,-93,34,40,47,-28,-6,-60,48],[42,-68,-14,-94,-36,-26,13,-96,-39,-71],[-96,1,37,-42,17,1,34,-30,-31,48],[-93,-24,12,-15,-98,49,30,-73,-4,16],[-86,-35,-100,4,15,14,-1,47,-11,46],[-76,-67,0,-95,25,5,-83,-54,45,30],[-27,-84,17,9,-63,-39,37,-69,-62,24],[-40,-37,-52,-39,10,-69,-73,-51,48,27],[5,-86,-92,-8,37,-44,33,0,-83,-37],[-82,45,23,-95,15,35,27,-28,-80,-80],[-57,26,-52,-13,-65,-80,-18,46,11,-14],[49,23,26,9,18,-57,-18,-82,-85,-10],[38,-25,-11,-38,44,-29,-14,-80,-16,4],[-46,48,39,-65,-59,-13,47,-23,-58,-100],[42,-69,-93,-18,22,5,-26,-77,-37,20],[30,41,-34,-93,-74,-49,-89,-53,-18,-51],[-3,12,28,8,28,-31,4,-75,-57,-89],[-70,0,-6,-74,-14,43,-53,-23,-76,-22],[14,-82,-25,-14,14,-78,-46,-16,28,-72],[5,48,45,-87,20,-13,-63,-48,-7,-64],[49,-3,-63,-43,-58,-23,-21,-60,11,15],[-65,-58,-50,47,45,-93,-71,20,-90,-58],[-49,-62,-16,11,43,-31,-39,13,-43,30],[8,-45,-98,-22,10,-46,-51,-22,-81,-99],[4,-87,-53,-53,-19,-38,24,-42,-15,-21],[-77,30,-95,39,42,10,41,-40,-46,-51],[-69,45,-99,14,-54,35,18,-46,11,-80],[-12,50,-12,50,45,-58,18,-19,29,-24],[-63,12,-14,-28,-48,42,-8,-67,-87,43],[9,-87,26,-29,-53,-70,-11,-43,-88,15],[-1,-12,15,-42,-44,41,22,-46,7,-31],[-13,6,11,13,-98,-96,-54,-95,-84,-34],[13,-47,-42,-94,-90,-86,50,-91,19,48],[-26,-66,-18,45,-72,-60,-7,40,37,-45],[-11,15,48,-70,-89,-92,25,-82,-36,23],[27,-11,-4,35,-32,-30,-33,50,29,-24],[-32,26,-10,-5,25,-30,18,-70,-98,-3],[-80,-45,-65,42,-84,-56,-50,-97,-13,-65],[19,-41,26,-11,-66,18,-52,-16,28,-22],[45,-23,-79,-44,-38,-100,8,11,-99,-67],[-8,-48,-20,-15,-11,-52,20,30,-43,24],[-49,23,-58,-73,18,43,26,1,-33,32],[-15,27,-49,-87,-72,-45,-56,-91,-30,-40],[3,-55,-22,-44,-71,-100,-53,-99,-85,14],[-34,-67,25,-93,-21,-4,-37,-92,12,-97],[-14,17,-72,-3,-25,-44,-26,-98,10,-68],[-90,-97,-1,-31,-44,-27,43,-77,-35,-77],[28,-53,-27,-100,-51,-45,45,-67,-70,-61],[-24,-38,40,36,39,2,43,-38,-64,3],[-77,-85,-54,-88,41,-85,-57,-100,-93,-75],[40,-98,-59,-60,-15,39,-64,32,-77,13],[-50,9,-64,28,-8,-61,-16,-79,-77,-69],[10,16,-54,47,-11,-4,-54,-10,3,-10],[-76,-62,-78,-23,-34,-97,-17,-67,-23,13],[-67,-27,-74,-62,-56,-36,-9,-51,6,37],[23,32,-93,-3,28,-35,-13,11,7,-99],[-20,-54,-54,-82,-36,8,25,38,43,32],[-97,-71,38,-73,27,-71,47,-69,-74,19],[-61,-10,5,-84,48,49,6,-86,-28,-48],[20,-92,-54,-7,2,-90,-68,14,-32,-12],[-27,-100,18,-47,5,-73,10,-50,-91,-75],[-30,-43,-31,-96,-34,-54,-72,-70,32,-72],[-51,-55,-17,24,39,39,-35,4,19,-82],[11,-14,-97,10,42,28,-31,-61,-96,38],[-94,-78,-42,10,-36,-72,2,-26,3,-68],[-44,23,5,-82,-81,-38,13,-76,0,-20],[-36,1,-90,-65,-67,-14,-79,46,35,30],[-85,-79,-34,46,-39,-79,8,-61,-75,-100],[-58,-54,-84,5,-93,-55,7,19,-27,-24],[1,-51,-30,-4,-39,-94,32,14,-46,-91],[37,-4,-18,-16,7,4,-98,-63,-15,44],[-4,-55,-33,30,-37,43,5,-13,-56,-17],[-19,-74,-31,-64,-50,-72,-63,50,1,-10]]

x = Solution()

print x.calculateMinimumHP(dungeon)