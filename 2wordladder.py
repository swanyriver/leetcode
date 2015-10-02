class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        #print wordList
        #return None
        
        irange = range(len(beginWord))
        
        foundwords = set()
        otherFoundwords = set()
        nextSet = set()
        nextSet.add(beginWord)

        otherNextSet = set()
        otherNextSet.add(endWord)

        chain = {}
        otherchain = {}        
        

        while nextSet:
            if set.intersection(nextSet,otherNextSet):
                #return stuff

            oldwords = list(nextSet)
            foundwords.update(nextSet)
            nextSet = set()
            
            for word in oldwords:
                for i in irange:
                    #print "replace:",replace
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        nextword = ''.join((word[:i], char, word[i+1:]))
                        #print "word:%r"%nextword
                        if nextword in wordList and nextword not in foundwords: nextSet.add(nextword)

            print oldwords, '->', nextSet

            otherFoundwords, foundwords = foundwords,otherFoundwords
            otherNextSet, nextSet = nextSet,otherNextSet





            
        
        # while nextSet :
        #     chainlength +=1
        #     oldwords = list(nextSet)
        #     wordsMade.update(nextSet)
        #     nextSet = []
            
        #     for word in oldwords:
        #         for i in irange:
        #             #print "replace:",replace
        #             for char in 'abcdefghijklmnopqrstuvwxyz':
        #                 nextword = ''.join((word[:i], char, word[i+1:]))
        #                 #print "word:%r"%nextword
        #                 if nextword == endWord: return chainlength
        #                 if nextword in wordList and nextword not in wordsMade: nextSet.append(nextword)
                            
            #print chainlength, len(nextSet), nextSet


                            
        return 0
        
x = Solution()
print x.ladderLength('hit','cog',["hot","dot","dog","lot","log"])
#print x.ladderLength()