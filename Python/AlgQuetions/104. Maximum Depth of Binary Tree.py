# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#      def __init__(self, val=0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right


class Solution:
    # Faster, but takes more memory
    # Runtime: 36 ms, faster than 92.25%
    # Memory Usage: 16.2 MB, less than 38.80%
    def maxDepth_recursion(self, root: TreeNode) -> int:
        # base case
        if root is None:
            return 0
        # recursion
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Time Сomplexity:
# - O(n), we visit every node only once
# Space Complexity:
# - O(log n) if case of balance tree
# - O(n) in worst case


# Slower, but takes less memory
# Runtime: 44 ms, faster than 49.47%
# Memory Usage: 15.4 MB, less than 92.42%


def maxDepth_stack(self, root: TreeNode) -> int:
    stack = []
    if root is not None:
        stack.append(1, root)

    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))
        return depth


# Time Сomplexity:
# - O(n), we visit every node only once
# Space Complexity:
# - O(log n) if case of balance tree
# - O(n) in worst case
