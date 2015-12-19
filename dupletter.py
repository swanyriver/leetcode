class number(object):
    def __init__(self,position,val):
        self.val = val
        self.position = position
    def __str__(self):
        return "pos%d,val%d"%(self.position,self.val)
    def __repr__(self):
        return self.str(self)

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map(list(enumerate(nums)),number)
        nums.sort(key=lambda x:x.val)
        
        print nums
        
x = Solution()
x.countSmaller([4,3,4,5,7,8,9,22])