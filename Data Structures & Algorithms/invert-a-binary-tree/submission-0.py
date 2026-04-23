# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root == []:
        #     return []
        queue = deque()
        queue.append(root)

        
        while len(queue) and queue[0]:
            curr = queue[0]
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            queue.popleft()
        return root