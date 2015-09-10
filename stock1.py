class local(object):
    """docstring for ClassName"""
    def __init__(self, min, max):
        #super(local, self).__init__()
        self.min = min
        self.max = max
    def __repr__(self):
        return "(%d,%d)"%(self.min,self.max)
    def diff(self): return self.max - self.min

        

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    # def maxProfit(self, k, prices):
    #     """
    #     :type k: int
    #     :type prices: List[int]
    #     :rtype: int
    #     """
        k=2

        # low = prices[0]
        # highestprofit =0

        # for p in prices:
        #     if p < low: low = p;
        #     elif p - low > highestprofit: highestprofit = p-low

        # return highestprofit
        slopes = []

        #mylocal = local(prices[0],None)
        i = 0
        while i<len(prices):
            mylocal = local(prices[i],None)
            while i<len(prices) and prices[i]<=mylocal.min:
                mylocal.min = prices[i]
                i+=1
            if i == len(prices):break
            mylocal.max = mylocal.min
            while i<len(prices) and prices[i]>=mylocal.max:
                mylocal.max = prices[i]
                i+=1
            slopes.append(mylocal)

        print prices
        print slopes
        print "------------------------------"

        # import matplotlib.pyplot as plt
        # plt.plot(prices, 'ro')
        # #for loc in slopes: plt.plot([loc.min,loc.max])
        # plt.ylabel('price')
        # plt.show()

        def elimc(s1,s2):
            return (s1.diff() + s2.diff()) - (s2.max - s1.min)

        for i in xrange(len(slopes)):
            if i<len(slopes)-1 and slopes[i+1].max > slopes[i].max:
                #calculate merge cost
                slopes[i].elimCost = elimc(slopes[i],slopes[i+1])
            else:
                slopes[i].elimCost = slopes[i].diff()
        
        for s in slopes:
            print s, s.elimCost



x = Solution()
# x.maxProfit([1,3,5,2,8,9,6])
# x.maxProfit([1,3,3,3,4,4,5,2,8,9,6])
# x.maxProfit([5,3,5,6,8,8,2,8,9,6])
x.maxProfit([5,3,5,6,8,8,2,8,9,6,10,1,3,4,0,3,1,9])
