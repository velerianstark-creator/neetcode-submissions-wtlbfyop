class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        memo = [False] * goal
        
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                memo[i] = True
                goal = i
        return memo[0] if memo else True
            
