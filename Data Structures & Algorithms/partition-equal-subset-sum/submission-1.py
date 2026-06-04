class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def checkPartition(rem, i):
            if rem == 0:
                return True
            if i == len(nums):
                return False
            if rem < nums[i]:
                return checkPartition(rem, i+1)
            return checkPartition(rem - nums[i], i+1) or checkPartition(rem, i+1)
        total = 0
        for num in nums:
            total += num
        if total % 2:
            return False
        half = total/2
        return checkPartition(half, 0)