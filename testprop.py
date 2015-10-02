n=4
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

attack = [ [False]*n for i in range(n) ]
while 1:
    #attack = [[False] * n] * n
    #attack = [ [False]*n for i in range(n) ]
    


    pair = raw_input("(x,y):")
    pair = map(int, pair.split(','))
    for line in propogateAttack(attack,pair[0],pair[1]): print line

    #for line in attack: print line
