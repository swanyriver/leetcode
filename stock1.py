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

    def add(self,s):
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

        heapq.heapify(pque)

        for s in pque:
            print s

        while len(slopes) > k:
            pass
            #get the next lowest

            #heap pop (while id not in slopes dict)

            #NOT MERGE
            #stich prev and next
            #remove from slopes dict

            #MERGE
            #create new item and remove both merged list from dict
            #cache prev and next objects from
            #add item to dictionary
            #set new items prev, next
            #set neighbors to point at new index
            #recaculate elimcost for neighbors



        #sum up diffs
            



x = Solution()
# x.maxProfit([1,3,5,2,8,9,6])
# x.maxProfit([1,3,3,3,4,4,5,2,8,9,6])
# x.maxProfit([5,3,5,6,8,8,2,8,9,6])
#x.maxProfit([5,3,5,6,8,8,2,8,9,6,10,1,3,4,0,3,1,9])

c = Chain()
for x in range(10): c.add( local(x,x+3))

