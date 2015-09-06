import bisect

def inthere(arr,val):
    index = bisect.bisect_left(arr,val)
    if index < len(arr) and arr[index] == val: return index
    else: return None

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not words: return []
        
        wordsinString = []
        answer = []
        words.sort()

        wordlength = len(words[0])

        for i in range(0,len(s) - wordlength + 1):
            wordsinString.append( inthere( words, s[i:i+wordlength] ) )


        #testing
        print words
        print s
        print wordsinString


        return answer


s = "barfoothefoobarman"
words = ["foo", "bar"]
o = Solution()
result = o.findSubstring(s,words)


print result
            
