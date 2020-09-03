
from math import log, ceil

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, prime) in enumerate(nums):
        
        if prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def upper_bound_for_p_n(number):
    if number < 6:
        return 100
    return ceil(number * (log(number) + log(log(number))))

def find_n_prime(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]

N = int(input())
z = find_n_prime(N)
print(z)