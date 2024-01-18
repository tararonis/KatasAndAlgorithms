# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # Time complexity: ~O(n^3)
    # Runtime: 460 ms, faster than 14.63%
    # Memory Usage: 14.3 MB, less than 82.54% of Python3
    def lengthOfLongestSubstring_naive(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 1
        let = set()
        for i, char1 in enumerate(s):  # O(n^2)
            let.add(char1)
            for char2 in s[i + 1 :]:
                if char1 == char2 or char2 in let:
                    result = max(len(let), result)
                    let.clear()

                    break
                let.add(
                    char2
                )  # Adding elements:- Insertion in set is done through set.add() function,
                # where an appropriate record value is created to store in the hash table.
                # Same as checking for an item, i.e., O(1) on average. However u=in worst case it can become O(n).

        return max(len(let), result)

    def lengthOfLongestSubstring_dict(self, s: str) -> int:
        # Time complexity: O(2n) -> O(n)
        # Runtime: 64 ms, faster than 70.19% of Python3
        # Memory Usage: 14.2 MB, less than 94.27% of Python3
        letters = {}
        tail = -1
        head = 0
        result = 0

        while head < len(s):
            if s[head] in letters:
                tail = max(tail, letters[s[head]])
            letters[s[head]] = head
            result = max(result, head - tail)
            head += 1

        return result


def main():
    test_strings = ["dvdf", "pwwkew", "au", "", " ", "abcabcbb"]
    s = Solution()
    for str in test_strings:
        print(
            s.lengthOfLongestSubstring_dict(str)
            == s.lengthOfLongestSubstring_naive(str)
        )


if __name__ == "__main__":
    main()
