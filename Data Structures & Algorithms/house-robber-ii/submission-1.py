class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2, prev3, prev4 = 0, 0, 0, 0
        count = len(nums)
        if count == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
            prev3, prev4 = max(prev3, prev4 + nums[i+1]), prev3
        return max(prev1, prev2, prev3, prev4)