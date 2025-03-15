"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def main():
    a = 999
    b = 999

    largest_palindrome = -1

    while a**2 > largest_palindrome:

        n = a * b
        if n > largest_palindrome and is_palindrome(n):
            largest_palindrome = n
        elif n < largest_palindrome or b < 100:
            a -= 1
            b = a
        else:
            b -= 1
    print(largest_palindrome)


if __name__ == "__main__":
    main()
