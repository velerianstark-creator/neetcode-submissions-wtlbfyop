class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(i, current):
            output.append(current)
            if i == len(nums):
                # output.append(current)
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                backtrack(j + 1, current + [nums[j]])
            # backtrack(i + 1, current)
        output = []
        backtrack(0,[])
        return output