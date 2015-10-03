def cursor(l):
    mid = (l-1)/2,l/2

    yield mid

    left = mid[1]-1,mid[0]
    right = mid[1],mid[0]+1

    while left[0] >= 0:
        yield left
        left = left[1]-1,left[0]
        yield right
        right = right[1],right[0]+1


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s: return s
        if s[:(len(s)+1)/2] == s[len(s)/2:][::-1]: return s

        for l,r in cursor(len(s)):
            while l>0 and r<len(s)-1 and s[l] is s[r]:
                l-=1
                r+=1

            if s[l] is s[r]:
                if l is 0: return s[:r:-1] + s
                if r is len(s)-1: return s + s[l-1::-1]
             

x = Solution()

print x.shortestPalindrome(s)