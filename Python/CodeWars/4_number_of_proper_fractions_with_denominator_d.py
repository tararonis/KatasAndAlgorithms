"""https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python"""

from math import gcd
import timeit
import functools


def proper_fractions_loop(n):  # timeout
    c = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            c += 1
    return c


def proper_fractions_sum(n):  # timeout
    return sum([(gcd(n, x) == 1) for x in range(1, n)])


def proper_fraction_opt(n):
    # find all prime factors (without repetitions) of n
    factors = set()
    i = 2
    input = n
    while i * i <= input:
        if input % i == 0:
            factors.add(i)
            input = input // i
        else:
            i = i + 1
    factors.add(input)
    # use Euler totient formula to find the amount of numbers coprime to n that are smaller than n
    result = n
    for j in factors:
        result = result * (1 - (1 / j))
    return int(result)


def main():
    # print(proper_fraction_opt(15))# == 8, '//', proper_fractions(8))  1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.
    # print(proper_fractions(1))# == 0, '//', proper_fractions(1))
    # print(proper_fractions(2))# == 1, '//', proper_fractions(2))
    # print(proper_fractions(5))# == 4, '//', proper_fractions(4))
    # print(proper_fractions(25))# == 20, '//', proper_fractions(25))

    # n = 1003428395383
    n = 1_000_000

    print(f"Math:\t{timeit.timeit(lambda: proper_fraction_opt(n), number = 1)}")
    print(
        f"Build in func:\t{timeit.timeit(lambda: proper_fractions_loop(n), number = 1)}"
    )
    print(f"Loop:\t{timeit.timeit(lambda: proper_fractions_loop(n), number = 1)}")


if __name__ == "__main__":
    main()
