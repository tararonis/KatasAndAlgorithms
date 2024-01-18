"""
Running Median

You are given a stream of numbers. Compute the median for each
new element.

Eg. Given [2, 1, 4, 7, 2, 0, 5], the alg should otput
          [2, 1.5, 2, 3.0, 2, 2, 2]
"""
import heapq  # https://en.wikipedia.org/wiki/Binary_heap#Summary_of_running_times


class Solution_naive:
    """Naive impplementation.
    Sort  - O(n * log(n)).
    We will do it n times, so total time complexity will be:
    n * (n * log(n))
    """

    def __init__(self, stream):
        self.stream = stream
        self.arr = []

    def running_median(self):
        for num in self.stream:
            self.arr.append(num)  # O(1)
            self.arr.sort()
            self.print_median(self.arr)

    def get_median(self, arr):
        if len(arr) == 1:
            return arr[0]
        half = int((len(arr) / 2))
        if len(arr) % 2 == 0:
            sum = arr[half - 1] + arr[half]
            return (arr[half - 1] + arr[half]) / 2
        elif len(arr) % 2 == 1:
            return arr[half]

    def print_median(self, arr):
        print(self.get_median(arr))


class Solution_with_heaps:
    """
    Implementation with 2 heaps.
    In "max" will be numbers that smaller then median,
    in "min" will be bigger numbers.

    - add number O(log(n))
    - rebalance heap O(log(n))
    - get median O(i)

    Total time complexity O(n * log(n))

    """

    def __init__(self, stream):
        self.stream = stream

    def get_median(self, min_heap, max_heap):
        if len(min_heap) > len(max_heap):
            return min_heap[0]
        elif len(min_heap) < len(max_heap):
            return -max_heap[0]
        else:
            min_root = min_heap[0]
            max_root = -max_heap[0]

            return (min_root + max_root) / 2.0

    def add(self, num, min_heap, max_heap):
        if len(min_heap) + len(max_heap) <= 1:
            heapq.heappush(max_heap, -num)
            return
        median = self.get_median(min_heap, max_heap)

        if num > median:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)

    def rebalance(self, min_heap, max_heap):
        if len(min_heap) > len(max_heap) + 1:
            root = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -root)
        elif len(max_heap) > len(min_heap) + 1:
            root = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, root)

    def running_median(self):
        min_heap = []
        max_heap = []  # we will negative numbers to this heap to keep the
        # biggest numbers as smallest

        for num in self.stream:
            self.add(num, min_heap, max_heap)
            self.rebalance(min_heap, max_heap)

            self.print_median(min_heap, max_heap)

    def print_median(self, min_heap, max_heap):
        print(self.get_median(min_heap, max_heap))


def main():
    stream = [2, 1, 4, 7, 2, 0, 5]

    n = Solution_naive(stream)
    n.running_median()

    h = Solution_with_heaps(stream)
    h.running_median()


if __name__ == "__main__":
    main()
