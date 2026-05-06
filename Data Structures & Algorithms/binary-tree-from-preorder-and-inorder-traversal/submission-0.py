# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = dict()
        for n in range(len(inorder)):
            inorder_map[inorder[n]] = n
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            mid = inorder_map[root.val]
            root.left = helper(pre_left+1, pre_left + (mid - in_left), in_left, mid-1)
            root.right = helper(pre_left + mid - in_left + 1, pre_right,  mid + 1, in_right)
            return root
        return helper(0,len(inorder) -1 ,0,len(inorder) -1)

        
        
                
