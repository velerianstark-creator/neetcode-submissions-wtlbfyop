class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0
        while i < j:
            l = heights[i]
            r = heights[j]
            if l >= r:
                area = r * (j - i)
                j -= 1
            else:
                area = l * (j - i)
                i += 1
            res = max(res, area)
        return res
        