class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jumpFromIndex(i, result):
            if result or i >= len(nums) - 1:
                result = True
                return True
            if nums[i] == 0:
                return False
            for j in range(nums[i], 0, -1):
                if jumpFromIndex(i + j, result):
                    result = True
                    return True
            return result
            
        return jumpFromIndex(0, False)
        