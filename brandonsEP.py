import math

def sievev1(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(2,MAX):
        if candidates[i]:
            primes.append(i)
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes

def sievev2(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(4,MAX,2): candidates[i]=False
    primes.append(2)

    for i in xrange(3,MAX,2):
        if candidates[i]:
            primes.append(i)
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes


sieve = sievev2

def isPrime(x):
    if x == 2 or x==3: return True
    if not x&1: return False
    if x < 2: return False
    if not x%3:
        return False
    r = int(math.sqrt(x))
    f = 5
    while f<=r:
        if not x%f or not x%(f+2):
            return False
        f+=6
    return True

def allDivisors(n, inclusive = False):
    divisors = [1]
    for factor in xrange(2,int(math.sqrt(n))+1):
        div = divmod(n,factor)
        if not div[1]:
            divisors.append(factor)
            divisors.append(div[0])
    if len(divisors)>1 and divisors[-1] == divisors[-2]: divisors.pop()
    if inclusive: divisors.append(n)
    return divisors

def fact(x):
    if x==0: return 1
    for i in range(x-1,0,-1): x*=i
    return x

def numCombs(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))
def numCombsWRep(n,r):
    return int(fact(n+r-1)/(fact(r)*fact(n-1)))
def numPerms(n,r):
    return int(fact(n)/fact(n-r))

def digits(x, reverse = False):
    result = []
    while x:
        a = divmod(x,10)
        result.append(a[1])
        x = a[0]
    if not reverse: result.reverse()
    return result

def lsToNum(digList):
    result = 0
    for digit in digList:
        result *=10
        result +=digit
    return result

#def contains(sortedlist,num):
    #This function is slower than python "in" wich i assumed was linear
    #is it stack frame genearation, or the list slices
#    if len(sortedlist) == 1:
#        return num == sortedlist[0]
#    else:
#        mid = len(sortedlist)//2
#        if num < sortedlist[mid]: 
#            return contains(sortedlist[:mid], num)
#        else:
#            return contains(sortedlist[mid:], num)

#From Rosseta Code
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return True
    return False

def binary_search_index(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return mid

def pythagPrims(Numlevels):

    """
    uses Berggren trees,  returns all primitive pythageran triples
    returns sum(3**i for i=0-numLevels) number of 3Tuples
    """

    matrixA = ((1,-2,2), (2,-1,2),(2,-2,3))
    matrixB = ((1,2,2), (2,1,2),(2,2,3))
    matrixC = ((-1,2,2), (-2,1,2),(-2,2,3))

    matricies = (matrixA,matrixB,matrixC)

    trips = [(3,4,5)]
    for i in range(Numlevels):
        #print i, trips[:-3**i]
        for discvovered in trips[-3**i:]:
            for m in matricies:
                trips.append(tuple(sum(k*v for k,v in zip(row,discvovered)) for row in m))


    return trips


def primeFactors(num):

    orig = num

    pFactors =[]
    
    #factors of 2
    if not num&1: pFactors.append(2)

    while not num&1:
        num = num>>1

    for i in range(3,orig):
        div = divmod(num, i)
        if not div[1]: pFactors.append(i)
        while div[0] and not div[1]:
            num = div[0]
            div = divmod(num, i)
        if not div[1]:
            if brandonsEP.isPrime(num): pFactors.append(num)

    return pFactors


def concatNums(a,b):
    from math import log10
    #lenb = int(log10(b))+1
    a*= 10**(int(log10(b))+1)
    return a+b


def lengthNum(x):
    return int(math.log10(x))+1


def polynumber(sides,n):
    s = sides
    return ((n**2)*(s-2) - n*(s-4))//2


def ceildiv(a, b):
    return -(-a // b)