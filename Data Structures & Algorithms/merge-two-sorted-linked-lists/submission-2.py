# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val >= list2.val:
            prev = list2
            curr = list2
            list2 = list2.next
        else:
            prev = list1
            curr = list1
            list1 = list1.next
        while list1 and list2:
            if list1 is not None:
               val1 = list1.val 
            if list2 is not None:
                val2 = list2.val
            if val1 >= val2:
                curr.next = list2
                curr = list2
                list2 = list2.next
            else:
                curr.next = list1
                curr = list1
                list1 = list1.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        else: curr.next = None
        return prev