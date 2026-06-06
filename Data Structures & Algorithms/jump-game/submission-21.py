class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        # if len(nums) == 1:
        #     return True
        # if nums[0] == 0:
        #     return False
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        return False
            
