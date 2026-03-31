class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in counter_dict:
                return [counter_dict.get(num), i]
            else:
                counter_dict[target - num] = i
        return []
                
        