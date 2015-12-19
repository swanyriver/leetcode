from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        A,C = min(A,C), max(A,C)
        B,D = min(B,D), max(B,D)

        E,G = min(E,G), max(E,G)
        F,H = min(F,H), max(F,H)

        xline = sorted((A,C,E,G))
        if (xline[1] == C and xline[2] == E) or (xline[1] == G and xline[2] == A): return 0

        yline = sorted((B,D,F,H))
        if (yline[1] == D and yline[2] == F) or (yline[1] == H and yline[2] == B): return 0

        
