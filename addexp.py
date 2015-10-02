def spread(num):
    lastRound = [(num[0],str(num[0]))]
    

    for digit in num[1:]:
        nextRound = []
        for x,formula in lastRound:
            nextRound.append( (x + digit, formula + '+%d'%digit) )
            nextRound.append( (x - digit, formula + '-%d'%digit) )
            nextRound.append( (x * digit, formula + '*%d'%digit) )
        lastRound = nextRound

    return nextRound



class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        num = map(int,num)
        return [x[1] for x in spread(num) if x[0] is target]


# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []

x = Solution()
##s = x.addOperators('123',8)
##for line in s: print line

#print x.addOperators('123',6)
print"""
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
--------------------------------
"""

tests = [("123", 6) ,
("232", 8),
("105", 5),
("00", 0), 
("3456237490", 9191)]

for s,t in tests[:-1]:
    print s,t, "-> ", x.addOperators(s,t) 
