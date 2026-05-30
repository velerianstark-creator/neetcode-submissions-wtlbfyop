class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            if i == 0:
                prev2 = nums[0]
                continue
            if i == 1:
                prev1 = max(nums[0], nums[1])
                continue
            prev2, prev1 = prev1, max(prev1, prev2+ nums[i])
        return max(prev1, prev2)
            