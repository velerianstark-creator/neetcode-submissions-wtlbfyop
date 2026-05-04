# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder_traversal(node, res):
            if not node:
                return
            inorder_traversal(node.left, res)
            res.append(node.val)
            inorder_traversal(node.right, res)
        inorder_traversal(root, res)
        return res[k-1]
        