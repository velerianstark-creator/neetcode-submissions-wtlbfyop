# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isValid(node, min_val, max_val):
            if not node:
                return True
            if min_val < node.val < max_val:
                return isValid(node.left, min_val, node.val) and isValid(node.right, node.val, max_val)
            return False
        return isValid(root.left, -math.inf, root.val) and isValid(root.right, root.val, math.inf)