class mlist(list):
    def __init__(self):
        self.sum = 0
    def append(self,x):
        super(mlist, self).append(x)
        self.sum += x
    def pop(self):
        self.sum -= super(mlist, self).pop()


def makeComb(answer, l, candidates, target, listlength):
    if not candidates:return
    #print "l:",l," candidates:", candidates
    while candidates[0] <= target - l.sum:
            l.append(candidates[0])
    if l.sum == target: answer.append(list(l))

    #print l

    while(len(l) > listlength):
        l.pop()
        #print "sending L: ", l, " candidates:", candidates[1:]
        makeComb(answer,l,candidates[1:],target,len(l))

        


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []

        candidates =sorted(set(candidates))

        answer = []

        # for i in range(len(candidates)):
        #     makeComb(answer,mlist(),candidates[i:],target)
        
        makeComb(answer,mlist(),candidates,target, 0)


        return answer 


x = Solution()
print x.combinationSum([3,2,6,7,1,4],7)
