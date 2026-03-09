def sum_k(n):
    return (n * (n + 1)) / 2


def sum_k_2(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def main():
    """
        We should be able to solve this with basic Calculus


    sum k = (n(n + 1)) / 2
    sum k^2 = (n(n + 1)(2n + 1)) / 6
    """
    sum_of_squares = sum_k_2(100)
    square_of_sum = sum_k(100) ** 2

    print(square_of_sum - sum_of_squares)


if __name__ == "__main__":
    main()
