"""
PROBLEM 7

Find the 10_001st prime number
"""

import math


def sieve_of_eratosthenes(start: int, end: int) -> list[int]:
    # [start, end)

    nums = [x for x in range(start, end)]

    i = 0
    primes = []
    while i < len(nums):
        prime = nums[i]
        primes.append(prime)

        l = []
        for j in range(i + 1, len(nums)):
            if nums[j] % prime != 0:
                l.append(nums[j])

        nums = primes + l

        i += 1
    return primes


def main():
    target_n = 10_001

    primes = sieve_of_eratosthenes(2, 300000)
    print(len(primes))

    if len(primes) >= 10_001:
        print(primes[10000])


if __name__ == "__main__":
    main()
