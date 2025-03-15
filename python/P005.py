"""
PROBLEM 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divisible(x: int) -> bool:

    for n in range(20, 1, -1):
        if x % n != 0:
            return False
    return True


def main():

    x = 20  # starting with something arbitrary
    while True:
        x += 20

        if divisible(x):
            print(x)
            break


if __name__ == "__main__":
    main()
