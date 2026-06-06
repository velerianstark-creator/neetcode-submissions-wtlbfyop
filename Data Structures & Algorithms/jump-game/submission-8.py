class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jumpFromIndex(i):
            if i >= len(nums) - 1:
                return True
            for j in range(nums[i], 0, -1):
                if jumpFromIndex(i + j):
                    return True
            return False
            
        return jumpFromIndex(0)
        