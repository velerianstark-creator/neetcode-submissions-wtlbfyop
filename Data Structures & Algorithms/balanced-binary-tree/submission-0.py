# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        minus = [0]
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            for child in [left, right]:
                if child == -1:
                    return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        if height(root) == -1:
            return False
        return True