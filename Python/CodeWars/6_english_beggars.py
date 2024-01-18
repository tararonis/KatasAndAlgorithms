"""
https://www.codewars.com/kata/59590976838112bfea0000fa/train/python
"""
# import numpy as np
from datetime import datetime


def beggars(values: list, n: int) -> list:
    if n == 0:
        return []
    answer = [0] * n  # [0 for x in range(n)]
    for i, change in enumerate(values):
        answer[i % n] += change

    return answer


def beggars2(values, n):
    return [sum(values[i::n]) for i in range(n)]


def test_cases():
    if all(
        (
            beggars([1, 2, 3, 4, 5], 1) == [15],
            beggars([1, 2, 3, 4, 5], 2) == [9, 6],
            beggars([1, 2, 3, 4, 5], 3) == [5, 7, 3],
            beggars([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5, 0],
            beggars([1, 2, 3, 4, 5], 0) == [],
        )
    ):
        # print("OK")
        pass
    else:
        print("Wrong")


def main():
    start = datetime.now()

    for _ in range(2000000):
        test_cases()

    print(datetime.now() - start)


if __name__ == "__main__":
    main()
