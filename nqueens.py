def propogateAttack(attack,x,y):
    n = len(attack)

    rAttack = []
    for l in attack: rAttack.append(list(l))

    for i in xrange(n):
        rAttack[i][y] = True
        rAttack[x][i] = True

    x2,y2=x,y
    while x2 >= 0 and y2 >= 0:
        rAttack[x2][y2]=True
        x2-=1
        y2-=1

    x2,y2=x,y
    while x2 < n and y2 < n:
        rAttack[x2][y2]=True
        x2+=1
        y2+=1

    x2,y2=x,y
    while x2 <n and y2 >=0:
        rAttack[x2][y2]=True
        x2+=1
        y2-=1

    x2,y2=x,y
    while x2 >=0 and y2 < n:
        rAttack[x2][y2]=True
        x2-=1
        y2+=1


    return rAttack

def placeQ(x,n,prevAtk, qplaces, answers):

    for y in range(n):

        # print "x,y:%d,%d"%(x,y)
        # pattack = [ [ 1 if row else 0 for row in col ] for col in prevAtk ]
        # for line in pattack: print line

        if not prevAtk[x][y]:

            # for line in prevAtk: print line
            # print "placing queen:(%d,%d)"%(x,y)
            # print '----------------------------'

            if x == n-1: 
                answers.append( qplaces + [y] )
            else:
                placeQ(x+1,n,propogateAttack(prevAtk,x,y),qplaces + [y], answers)


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        answer = []
        attack = [ [False]*n for i in range(n) ]


        placeQ(0,n,attack,[],answer)

        #return answer

        return [ ["".join(['Q' if x==row else '.' for x in range(n)]) for row in solv] for solv in answer ]

n = 4
x = Solution()
print x.solveNQueens(n)




