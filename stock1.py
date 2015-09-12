class local(object):
    """A connection from local minimum to local maximum"""
    def __init__(self, Min, Max):
        #super(local, self).__init__()
        self.min = Min
        self.max = Max
    def __repr__(self):
        return "(%d,%d)"%(self.min,self.max)
    def __str__(self): return self.__repr__()
    def diff(self): return self.max - self.min

class Chain(object):
    """doubly linked list of locals"""
    def __init__(self):
        self.begining = None
        self.end = None
        self.count = 0
    def __len__(self):
        return self.count

    def append(self,s):
        s.prev = self.end
        s.next = None
        self.end = s
        self.count +=1
        if not self.begining:
            self.begining = s
            self.end = s
        else:
            s.prev.next = s

    def remove(self,s):
        self.count -=1
        if not self.count:
            self.begining = None
            self.end = None
        elif s is self.begining:
            self.begining = s.next
            self.begining.prev = None
        elif s is self.end:
            self.end = s.prev
            self.end.next = None
        else:
            s.prev.next = s.next
            s.next.prev = s.prev

    def __iter__(self):
        snext = self.begining
        while snext:
            yield snext
            snext = snext.next

    def __repr__(self):
        return "->".join(map(str,self))
    def __str__(self): return self.__repr__()


        

class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     k=2
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if len(prices)<2 or k <1: return 0


        


        slopes = Chain()


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

        # print prices
        # print slopes
        # print "------------------------------"

        def elimc(s):
            if s.next and s.next.max > s.max and s.next.min > s.min: 
                s.merge = True
                s.elimcost= (s.diff() + s.next.diff()) - (s.next.max - s.min)
            else : 
                s.merge = False
                s.elimcost = s.max-s.min
            return s
        # def attachelim(s):
        #     s.elimcost = elimc(s)
        #     return s

        map(elimc,slopes)

        # for s in slopes:
        #     print s, s.elimcost
        # print len(slopes)

        while len(slopes) > k:
            #get the next lowest
            smallest = slopes.begining
            for s in slopes:
                if s.elimcost < smallest.elimcost: smallest = s

            if not smallest.merge: 
                slopes.remove(smallest)
            else:
                smallest.next.min = smallest.min
                elimc(smallest.next)
                slopes.remove(smallest)

            if smallest.next: elimc(smallest.next)
            if smallest.prev: elimc(smallest.prev)

            #print slopes,
            #print sum(map(lambda s:s.diff(),slopes))



        #sum up diffs
        return sum(map(lambda s:s.diff(),slopes))
            



x = Solution()
# x.maxProfit([1,3,5,2,8,9,6])
# x.maxProfit([1,3,3,3,4,4,5,2,8,9,6])
# x.maxProfit([5,3,5,6,8,8,2,8,9,6])
#x.maxProfit([5,3,5,6,8,8,2,8,9,6,10,1,3,4,0,3,1,9])
print x.maxProfit(2, [2,6,8,7,8,7,9,4,1,2,4,5,8])


