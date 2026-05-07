class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
               
        def backtrack(i, current, n):
            if i == n:
                output.append(current)
                return
            backtrack(i+1, current + [nums[i]], n)
            backtrack(i+1, current, n)
        output = []
        backtrack(0, [], len(nums))
        return output