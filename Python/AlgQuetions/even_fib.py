# https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison
from collections import deque


def even_fibonacci_numbers(n: int) -> deque:
    """
    Function returns deque of first n even Fibonachi numbers

    Time complexity: O(n)
    Space complexity: O(n)
    """
    even_series = deque()
    first, second = 0, 1  # Starting numbers
    i = 0  # Index of first number in the Fibonacci sequence

    while len(even_series) < n:
        if first % 2 == 0:
            even_series.append(first)

        first, second = second, first + second  # Calculate next Fibonacci number
        i += 1

    return even_series


def main():
    # a = even_fibonacci_numbers(20)
    # print(a)
    print(even_fibonacci_numbers(4) == [0,2,8,34])


if __name__ == "__main__":
    main()
