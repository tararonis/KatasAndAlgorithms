"""Compare different methods to loop"""
import timeit
import numpy as np


def while_loop(n=200_000_000):
    sum = 0
    i = 0
    while i < n:
        sum += i
        i += 1


def for_loop(n=200_000_000):
    sum = 0
    for i in range(n):
        sum += i


def sum_range(n=200_000_000):
    return sum(range(n))


def sum_numpy(n=200_000_000):
    """Problem that numpy creates an array size n that
    takes enormous amount of memory. Anyway, it's the fastest way"""
    return np.sum(np.arange(n))


def main():
    print(f"While loop:\t\t {timeit.timeit(while_loop, number=1)}")
    print(f"Pure for:\t\t {timeit.timeit(for_loop, number=1)}")
    print(f"Sum range:\t\t {timeit.timeit(sum_range, number=1)}")
    print(f"Numpy sun:\t\t {timeit.timeit(sum_numpy, number=1)}")


if __name__ == "__main__":
    main()
