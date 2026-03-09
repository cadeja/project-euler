"""
PROBLEM 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def get_factors(n: int) -> list[int]:
    # include repeating factors

    l = []
    i = 2
    while i <= n:
        if n % i == 0:
            l.append(i)
            n /= i
        else:
            i += 1
    return l


def solve_for_n(n: int) -> int:

    factor_count_max = {}

    for x in range(n, 1, -1):
        factors = get_factors(x)

        factor_count = {}
        # iterate and count occurences
        for factor in factors:
            if factor not in factor_count:
                factor_count[factor] = 1
            else:
                factor_count[factor] += 1

        # compare to outer dict
        for k, v in factor_count.items():
            if k not in factor_count_max:
                factor_count_max[k] = v
            else:
                if factor_count_max[k] < v:
                    factor_count_max[k] = v

    # calculate
    result = 1
    for k, v in factor_count_max.items():
        result *= k**v

    return result


def main():
    # if you get the prime factors of 1-20 and multiply the highest powers, you get the answer
    # can we make a program that will calculate this for any range?

    print(solve_for_n(20))


if __name__ == "__main__":
    main()
