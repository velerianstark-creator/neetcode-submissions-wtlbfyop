# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        l = head
        r = prev

        while r:
            l_next = l.next
            r_next = r.next
            l.next = r
            r.next = l_next
            l = l_next
            r = r_next

        # return head