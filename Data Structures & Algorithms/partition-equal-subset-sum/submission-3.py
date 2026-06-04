class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def checkPartition(rem, i):
            if (rem, i) in memo:
                return memo[(rem, i)]
            if rem == 0:
                memo[(rem, i)] = True
                return True
            if i == len(nums):
                memo[(rem, i)] = False
                return False
            if rem < nums[i]:
                return checkPartition(rem, i+1)
            return checkPartition(rem - nums[i], i+1) or checkPartition(rem, i+1)
        memo = {}
        total = 0
        for num in nums:
            total += num
        if total % 2:
            return False
        half = total//2
        return checkPartition(half, 0)