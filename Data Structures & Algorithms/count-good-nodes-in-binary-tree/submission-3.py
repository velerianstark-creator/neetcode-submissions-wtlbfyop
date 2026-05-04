# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #max_node = [root.val]
        def track(node: TreeNode, max_val: int) -> int:
            if not node:
                #max_node[0]= root.val
                return 0
            if node.val < max_val:
                return track(node.left, max_val) + track(node.right, max_val)
            # max_node[0] = node.val
            return 1 + track(node.left, node.val) + track(node.right, node.val)
        return track(root, root.val)