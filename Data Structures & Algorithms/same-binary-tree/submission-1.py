# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        compare = [True]
        def compare2node(p_node: Optional[TreeNode], q_node: Optional[TreeNode]) -> None:
            if not compare[0]:
                return False
            if not (p_node is None) is (q_node is None):
                compare[0] = False
            elif p_node:
                if p_node.val != q_node.val:
                    compare[0] = False
                compare2node(p_node.left, q_node.left)
                compare2node(p_node.right, q_node.right)     
        compare2node(p, q) 
        return compare[0]
            
