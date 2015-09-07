from itertools import combinations

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        cadidates = sorted(set(candidates))
        
        answer = []
        
        if target in candidates: answer.append( (target,) )

        for r in xrange(2,len(candidates)+1):
            combs = combinations(candidates,r)
            answer.extend( [ x for x in combs if sum(x)==target ] )
            
        return answer

x = Solution()
print x.combinationSum2([10,1,2,7,6,1,5],8)