class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jumpFromIndex(i):
            if i not in memo:
                if i >= len(nums) - 1:
                    return True
                if nums[i] == 0:
                    memo.add(i)
                    return False
                for j in range(nums[i], 0, -1):
                    if jumpFromIndex(i + j):
                        return True
            memo.add(i)
            return False
        memo = set()
        return jumpFromIndex(0)
        