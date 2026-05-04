# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque([root])
       
        while queue:
            size = len(queue)
            for n in range(size):
                node = queue.popleft()
                if node:
                    if n == 0:
                        output.append(node.val)
                    for child in [node.right, node.left]:
                        if child:
                            queue.append(child)
        return output
        