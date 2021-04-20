"""https://www.codewars.com/kata/59e19a747905df23cb000024/train/python"""

from collections import OrderedDict
from collections import Counter
import timeit


def string_letter_count2(s):
    od = OrderedDict()
    for c in s.lower():
        if c.isalpha():
            if c in od:
                od[c] += 1
            else:
                od[c] = 1
    od = OrderedDict(sorted(od.items()))
    ans = "".join(["{}{}".format(v, k) for k, v in od.items()])
    return ans


def string_letter_count1(s):
    s = s.lower()
    m = ""
    for i in sorted(list(set(s))):
        if i.islower():
            m += str(s.count(i)) + i
    return m


def string_letter_count(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return "".join(str(n) + c for c, n in sorted(cnt.items()))


def main():
    print(
        f'OrderDICT:\t{timeit.timeit(lambda: string_letter_count2("This is a test sentence."), number=1000_000)}'
    )
    print(
        f"Set:\t{timeit.timeit(lambda: string_letter_count1('This is a test sentence.'),number=1000_000)}"
    )
    print(
        f"Counter:\t{timeit.timeit(lambda: string_letter_count('This is a test sentence.'),number=1000_000)}"
    )


if __name__ == "__main__":
    main()
