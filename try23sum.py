import bisect

class Solution(object):

    def inthere(self,arr,val, lo, hi):
        index = bisect.bisect_left(arr,val,lo=lo,hi=hi)
        if index < hi and arr[index] == val: return True
        else: return False

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) <3: return []
        
        nums.sort()

        zerospot = bisect.bisect_left(nums,0)
        zzerospot = bisect.bisect_right(nums,0)
        answer = []


        if zerospot == 0 or zerospot == len(nums): return []

        print zerospot

        i = 0
        while(i<zzerospot):
            print "[", i , "]:", nums[i]
            if len(nums) - i < 3: break


            largevalindex = bisect.bisect_right(nums, ( nums[i] + nums[i+1]) * -1 ) - 1;

            print "first largevalindex:", largevalindex, " searching for:", ( nums[i] + nums[i+1]) * -1, "("

            while largevalindex >= zerospot:

                print "largevalindex:", largevalindex, " searching for:", ( nums[i] + nums[i+1]) * -1, "(",

                compliment = (nums[i] + nums[largevalindex]) * -1

                print nums[i], compliment, nums[largevalindex], ")"


                if self.inthere(nums,  compliment, lo=i+1, hi=largevalindex ): answer.append([nums[i], compliment, nums[largevalindex]])

                while(nums[largevalindex-1] == nums[largevalindex]): largevalindex-=1
                largevalindex -= 1

            while(nums[i+1] == nums[i]): i +=1
            i+=1


        return answer      

arr = [6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]

print sorted(arr)
x = Solution()
a = Solution.threeSum(x,arr)
print a