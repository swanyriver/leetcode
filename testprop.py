n=4
def propogateAttack(attack,x,y):
    n = len(attack)

    for i in xrange(n):
        attack[i][y] = True
        attack[x][i] = True


    x2,y2 = x,y
    if x2 == y2: x2,y2 = 0,0
    elif x2>y2: x2 -= y2 
    else: y2 -= x
    while x2<n and y2<n:
        attack[x2][y2] = True
        x2 +=1
        y2 +=1


    x2 = 0
    y2 = x+y
    if y2 > n:
        x2 = y2 - n
        y2 = n-1
    while x2<n and y2 >= 0:
        attack[x2][y2] = True
        x2 +=1
        y2 -=1

while 1:
    #attack = [[False] * n] * n
    attack = [ [False]*n for i in range(n) ]
    


    pair = raw_input("(x,y):")
    pair = map(int, pair.split(','))
    propogateAttack(attack,pair[0],pair[1])

    for line in attack: print line
