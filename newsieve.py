def newsieve(n):
    primes = [2]

    nums = [x for x in range(3,n+1) if x & 1 ]

    while nums:
        primes.append(nums[0])
        nums = [x for x in nums if x%nums[0]]

    return primes