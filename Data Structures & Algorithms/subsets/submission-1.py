class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
               
        def backtrack(i, current):
            if i == len(nums):
                output.append(current)
                return
            backtrack(i+1, current + [nums[i]])
            backtrack(i+1, current)
        output = []
        backtrack(0, [])
        return output