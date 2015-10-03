def iFib(n):
    fib = 0
    a = 1
    t = 0
    for x in xrange(n):
        t = fib + a
        a = fib
        fib = t

    return fib

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s: return 0
        for i in range(len(s)):
            if s[i]=='0' and (i == 0 or s[i-1] not in "12"): return 0
        
        possibleways = 1
        i = 0
        
        while i < len(s):
            j = i
            while j < len(s)-1 and ( (s[j] == '2' and s[j+1] in "123456") or (s[j] == '1' and s[j+1] != '0' ) ): j+=1
            if j>i: 
                #subs.append(s[i:j+1])
                
                if j<len(s)-1 and s[j+1] == '0': j-=1 
                #print "i:%d,j:%d, s[i:j]:%r, j-i+1:%d, fib:%d"%(i,j,s[i:j+1],(j-i)+1, iFib((j-i)+2)  )
                possibleways *= iFib((j-i)+2)
                i=j
            i+=1

        return possibleways
        
