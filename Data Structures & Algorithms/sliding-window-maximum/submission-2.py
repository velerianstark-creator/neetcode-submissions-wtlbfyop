class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_v = float('-inf')
        pos = -1



        for i in range(0, len(nums) - k + 1):
            if i <= pos:
                if max_v > nums[i + k -1]:
                    res.append(max_v)
                elif max_v < nums[i + k -1]:
                    pos = i + k - 1
                    max_v = nums[i + k -1]
                    res.append(max_v)     
                else:
                    pos = i + k - 1
                    res.append(max_v)
            else:
                max_v = float('-inf')
                for j in range(i, i + k):
                    if nums[j] >= max_v:
                        max_v = nums[j]
                        pos = j
                res.append(max_v)

        return res
                