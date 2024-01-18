# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

from functools import reduce

def digital_root_2(n):
    while n > 9:
        n = sum_digits(n)
    return n

def sum_digits(n):
    return reduce(lambda x, y: x + y, map(int, str(n)), 0)


digital_root = lambda n: n if n < 10 else digital_root(reduce(lambda x, y: x + y, map(int, str(n)), 0))


def main():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2


if __name__ == "__main__":
    main()
