def cursor(l):
    mid = (l-1)/2,l/2

    yield mid

    left = mid[1]-1,mid[0]
    right = mid[1],mid[0]+1

    while left[0] >= 0:
        yield left
        left = left[1]-1,left[0]
        yield right
        right = right[1],right[0]+1

