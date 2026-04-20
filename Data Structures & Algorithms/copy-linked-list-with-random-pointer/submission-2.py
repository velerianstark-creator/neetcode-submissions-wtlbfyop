"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        if not head:
            return None
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node       
            curr = new_node.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            if curr.next:
                curr = curr.next.next
            else:
                break
        curr = head
        copy = head.next
        response = head.next
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
            if copy.next:
                copy.next = copy.next.next
                copy = copy.next
        return response