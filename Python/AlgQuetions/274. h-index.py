# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        According to the definition of h-index on Wikipedia:
         "A scientist has index h if h of his/her N papers have
          at least h citations each, and the other N − h papers
          have no more than h citations each."

        Args:
            citations (List[int]): input

        Returns:
            int: [description]

        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(citations)
        cit_list = [0] * (n + 1)

        for cit in citations:
            if cit < n:
                cit_list[cit] += 1
            else:
                cit_list[n] += 1

        total = 0
        i = n
        while i >= 0:
            total += cit_list[i]
            if total >= i:
                return i
            i -= 1
        return i


def main():
    citations = [3, 0, 6, 1, 5]
    s = Solution
    print(s.hIndex(s, citations))


if __name__ == "__main__":
    main()
