def propogateAttack(attack,x,y):
    n = len(attack)

    rAttack = []
    for l in attack: rAttack.append(list(l))

    for i in xrange(n):
        rAttack[i][y] = True
        rAttack[x][i] = True

    x2,y2 = x,y
    if x2 == y2: x2,y2 = 0,0
    elif x2>y2: x2 -= y2 
    else: y2 -= x
    while x2<n and y2<n:
        rAttack[x2][y2] = True
        x2 +=1
        y2 +=1

    x2 = 0
    y2 = x+y
    if y2 >= n:
        x2 = y2 - n
        y2 = n-1
    while x2<n and y2 >= 0:
        rAttack[x2][y2] = True
        x2 +=1
        y2 -=1

    return rAttack

def placeQ(x,n,prevAtk, qplaces, answers):

    for y in range(n):

        # print "x,y:%d,%d"%(x,y)
        # pattack = [ [ 1 if row else 0 for row in col ] for col in prevAtk ]
        # for line in pattack: print line

        if not prevAtk[x][y]:
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

        return answer

x = Solution()
print x.solveNQueens(4)


