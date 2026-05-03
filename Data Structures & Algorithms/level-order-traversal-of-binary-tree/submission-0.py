# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])
        while queue:
            sub_result = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    sub_result.append(node.val)
                    for child in [node.left, node.right]:
                        if child:
                            queue.append(child)
                # else:
                #     sub_result.append(None)
            if sub_result:
                result.append(sub_result)
        return result