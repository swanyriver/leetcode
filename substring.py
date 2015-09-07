import bisect

def inthere(arr,val):
    index = bisect.bisect_left(arr,val)
    if index < len(arr) and arr[index] == val: return index
    else: return None

def nonesplit(l):
    i = 0
    result = []
    while i<len(l):
        while i<len(l) and l[i].wordindex is None: i+=1
        if i >=len(l):break
        firstindex = i
        while i<len(l) and l[i].wordindex is not None: i+=1
        result.append(l[firstindex:i])
    return result
    
class wordspot:
    def __init__(self, stringindex, wordindex):
        self.wordindex = wordindex
        self.stringindex = stringindex

    def __str__(self):
        return str(self.stringindex) + "->" + str(self.wordindex)
    def __repr__(self):
        return str(self.stringindex) + "->" + str(self.wordindex)
        

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
            #wordsinString[listgroup%wordlength].append( inthere( words, s[i:i+wordlength] ) )

            #possilble optimization
            nextw = wordspot( i,  inthere( words, s[i:i+wordlength] ))
            if not len(wordsinString[listgroup%wordlength]) or nextw.wordindex is not None or wordsinString[listgroup%wordlength][-1].wordindex is not None:
                wordsinString[listgroup%wordlength].append( nextw )

            #wordsinString[listgroup%wordlength].append( wordspot( i,  inthere( words, s[i:i+wordlength] )) )
            listgroup+=1


        # #testing
        # #print words
        # #print s
        # #print wordsinString

        wordsinString = [nonesplit(x) for x in wordsinString]
        wordsinString = [ [ x for x in group if len(x) >= len(words) ] for group in wordsinString]
        wordsinString = [x for x in wordsinString if x ]
        wordsinString = [item for sublist in wordsinString for item in sublist]

        # #print "splited:"
        #print wordsinString

        for group in wordsinString:

            print group

            #magic code goes here
            count = 0
            used = [False]*len(words)
            firstwordindex=0
            lastindex = 0

            while lastindex < len(group):

                print "----------------------------------------"
                print "      count: ", count, " used:", used

                if not used[group[lastindex].wordindex]:
                    used[group[lastindex].wordindex]=True
                    count+=1
                    if count == len(words): 
                        answer.append(group[firstwordindex].stringindex)
                        count-=1
                        used[group[firstwordindex].wordindex]=False
                        firstwordindex+=1

                else:

                    while firstwordindex < lastindex and group[firstwordindex].wordindex != group[lastindex].wordindex:
                        used[group[firstwordindex].wordindex]=False
                        firstwordindex+=1
                        count-=1
                    firstwordindex +=1

                lastindex+=1

                print "after count: ", count, " used:", used

        return answer


#s = "barfoothefoobarmannbarfooobar"
#words = ["foo", "bar", "buz"]
#s = "foobarbuzfoobarapplefoobarfoobuzbarbuzfoo"
s,words = "wordgoodgoodgoodbestword", ["word","good","best","good"]
o = Solution()
result = o.findSubstring(s,words)


print result
            
