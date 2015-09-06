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

        wordlength = len(words[0])
        
        
        answer = []
        words.sort()

        
        # wordsinString = []
        # for i in range(0,len(s) - wordlength + 1):
        #     wordsinString.append( inthere( words, s[i:i+wordlength] ) )

        wordsinString =  [ [] for x in range(wordlength)  ]
        listgroup = 0

        for i in range(0,len(s) - wordlength + 1):
            wordsinString[listgroup%wordlength].append( inthere( words, s[i:i+wordlength] ) )
            listgroup+=1



        #testing
        print words
        print s
        print wordsinString


        return answer


s = "barfoothefoobarmannbarfooobar"
words = ["foo", "bar"]
o = Solution()
result = o.findSubstring(s,words)


print result
            
