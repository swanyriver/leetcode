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

        keypoints = []
        keypoints.append([buildings[0][l],buildings[0][h]])

        for bldg in buildings:
            


answer = [ [2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0] ]
buildings = [ [2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8] ]

x = Solution();

result = x.getSkyline(buildings);
print "solution:", answer
print " myfunct:",result
print answer == result