"""
Find the pythagorean triplet for:
a + b + c = 1000
return the product abc

A Pythagorean triplet is a set of 3 numbers:
a < b < c
for which a**2 + b**2 = c**2
"""


def problem():
    # we know that a + b > c
    # a < 500, b < 500, c < 500

    for a in range(1, 500):
        for b in range(a, 500):
            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                return a * b * c


def main():
    print(problem())


if __name__ == "__main__":
    main()
