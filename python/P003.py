"""
PROBLEM 3

The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?
"""

import math


def main():

    x = 600_851_475_143
    x_squared = math.sqrt(x)

    highest_factor = -1
    n = 2
    while n <= x_squared and x != 1:  # highest possible factor is square root

        if x % n == 0:
            highest_factor = n
            x /= n
        else:
            if n == 2:
                n = 3
            else:
                n += 2

    print(highest_factor)


if __name__ == "__main__":
    main()
