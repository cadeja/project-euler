"""
PROBLEM 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum
of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    # make a set of multiples of 3 under 1000, and another set with multiples of 5 under 1000
    # union the sets
    # find the sum

    set_a = {x for x in range(3, 1000, 3)}
    set_b = {x for x in range(5, 1000, 5)}
    print(sum(set_a.union(set_b)))


if __name__ == "__main__":
    main()
