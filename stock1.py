import heapq
class local(object):
    """docstring for ClassName"""
    def __init__(self, Min, Max, prev):
        #super(local, self).__init__()
        self.min = Min
        self.max = Max
        self.prev = prev
        self.next = None
    def __repr__(self):
        return "(%d,%d) id:%r p:%r, n:%r"%(self.min,self.max, self.ID, self.prev, self.next)
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

        class slopeDict(dict):
            """docstring for ClassName"""
            def __init__(self):
                #super(ClassName, self).__init__()
                self.lastAddedID = None
                self.nextId = 1
            def append(self, s):
                self[self.nextId]=s
                s.ID = self.nextId
                if self.lastAddedID: self[self.lastAddedID].next = self.nextId
                self.lastAddedID = self.nextId
                self.nextId+=1
                

        slopes = slopeDict()



        i = 0
        while i<len(prices):
            mylocal = local(prices[i],None,slopes.lastAddedID)

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

        # def elimc(s1,s2):
        #     return (s1.diff() + s2.diff()) - (s2.max - s1.min)
        def elimc(s):
            if s.next and slopes[s.next].max > s.max: 
                s.merge = True
                return (s.diff() + slopes[s.next].diff()) - (slopes[s.next].max - s.min)
            else : 
                s.merge = False
                return s.max-s.min

        pque = []

        for s in slopes.values():
            pque.append( (elimc(s),s) )
        # for i in xrange(len(slopes)):
        #     if i<len(slopes)-1 and slopes[i+1].max > slopes[i].max:
        #         #calculate merge cost
        #         slopes[i].elimCost = elimc(slopes[i],slopes[i+1])
        #     else:
        #         slopes[i].elimCost = slopes[i].diff()
        #     #pque.append(slopes[i])
            ##need to make a tuple 

        heapq.heapify(pque)
        for s in pque:
            print s

        #while len(slopes) > k:
            



x = Solution()
# x.maxProfit([1,3,5,2,8,9,6])
# x.maxProfit([1,3,3,3,4,4,5,2,8,9,6])
# x.maxProfit([5,3,5,6,8,8,2,8,9,6])
x.maxProfit([5,3,5,6,8,8,2,8,9,6,10,1,3,4,0,3,1,9])
