# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == []:
            return root
        queue = deque()
        queue.append(root)

        
        while len(queue):
            curr = queue.popleft()
            if not curr:
                continue
            curr.left, curr.right = curr.right, curr.left
            queue.append(curr.left)
            queue.append(curr.right)
                
            
        return root