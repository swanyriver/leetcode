#from collections import defaultdict

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        l = 0;
        r = 1;
        h = 2;

        if not buildings: return buildings

        lEdg = buildings[0][l]
        rEdg = buildings[-1][r]

        heights = [0]*((rEdg - lEdg )+1)
        #heights = [0] * (rEdg+1)
        keypoints = []

        for bldg in buildings:
            print bldg
            for x in xrange(bldg[l],bldg[r]):
                #heights[x-lEdg].append(bldg[h])
                #if x not in heights or bldg[h] > heights[x-lEdg]:
                if  bldg[h] > heights[x-lEdg]:
                    heights[x-lEdg]=bldg[h]
            #if bldg[r] not in heights: heights[bldg[r]] = 0

        print heights;

        hp = 0 
        
        #for x in sorted(heights.keys()):
        for x in range(len(heights)):
            if heights[x] != hp: 
                keypoints.append ([x+lEdg,heights[x]])
                hp = heights[x]
        return keypoints

answer = [ [2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0] ]
buildings = [ [2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8] ]

x = Solution();

result = x.getSkyline(buildings);
print "solution:", answer
print " myfunct:",result
print answer == result