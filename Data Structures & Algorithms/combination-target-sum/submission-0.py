class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, target, current):
            if target == 0:
                output.append(current)
                return
            if target < 0:                 
                return
            for j in range(i, len(nums)):
                backtrack(j, target - nums[j], current + [nums[j]])
   
        output = []
        backtrack(0, target, [])
        return output