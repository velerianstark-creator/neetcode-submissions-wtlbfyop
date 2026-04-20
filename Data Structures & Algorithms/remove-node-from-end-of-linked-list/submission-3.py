# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        for _ in range(n):
            if curr:
                curr = curr.next
            else:
                return None
        pivot = head
        prev = dummy
        while curr:
            prev = pivot
            curr = curr.next
            pivot = prev.next
        prev.next = pivot.next
        pivot.next = None
        return dummy.next
        