class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            prev2, prev1 = prev1, max(prev1, prev2+ nums[i])
        return max(prev1, prev2)
            