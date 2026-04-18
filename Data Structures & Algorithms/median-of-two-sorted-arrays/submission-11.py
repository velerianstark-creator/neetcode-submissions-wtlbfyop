import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums = nums1
            nums1 = nums2
            nums2 = nums
        l1 = len(nums1)
        l2 = len(nums2)
        l = 0
        r = len(nums1)

        
        while l <= r:
            i = (l + r) // 2
            j = (l1 + l2 + 1) // 2 - i
            A_left_max  = -math.inf if i == 0 else nums1[i - 1]
            A_right_min = math.inf if i == l1 else nums1[i]
            B_left_max  = -math.inf if j == 0 else nums2[j - 1]
            B_right_min = math.inf if j == l2 else nums2[j]
                
            if A_left_max > B_right_min:
                r = i - 1
            elif B_left_max > A_right_min:
                l = i + 1
            else:
                if (l1 + l2) % 2 == 1:
                    return max(A_left_max, B_left_max)
                else:
                    return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min))/2.0
        
