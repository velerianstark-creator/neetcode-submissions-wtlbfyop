class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(i, current):
            if i == len(nums):
                output.append(current.copy())
                return
            for j in range(i, len(nums)):
                current[i], current[j] = current[j], current[i]
                swap(i+1, current)
                current[i], current[j] = current[j], current[i]

        output = []
        swap(0, nums)
        return output