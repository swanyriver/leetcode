import math
factorial = range(0,10)
print "int factorial[10]={",
for x in range(2,10):
    factorial[x] = factorial[x-1] * x
    print factorial[x], ",",
print "}"

exit()

def getPermutation( n, k):
    nums = range(1,n+1)

    #on zero reverse remainder list

    out = ""

    for x in reversed(range(1,n)) or [1]:
        nextnum = int(math.ceil(float(k)/factorial[x]))-1
        out += str(nums[nextnum])
        del nums[nextnum]

        k=k%factorial[x]

        if k==0:
            while len(nums): out += str(nums.pop())
            return out
    return out
