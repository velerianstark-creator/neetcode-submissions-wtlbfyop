# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        sum_list = 0
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val

            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
            val = (val1 + val2 + carry) % 10
            curr.next = ListNode(val)
            carry = (val1 + val2 + carry) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        return dummy.next
                