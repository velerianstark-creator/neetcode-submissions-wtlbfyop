class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here, max_so_far = -float('inf'), -float('inf')
        for num in nums:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far