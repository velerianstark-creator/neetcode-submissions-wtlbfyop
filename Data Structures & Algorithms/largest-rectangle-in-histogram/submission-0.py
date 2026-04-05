class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = sorted(set(heights), reverse = True)
        max_a = 0

        while len(h) > 0:
            j = 0
            for i in range(len(heights)):
                if heights[i] >= h[- 1]:
                    j += 1
                    max_a = max(max_a, h[- 1] * j)
                else:
                    # heights[i] = 0
                    j = 0
            h.pop()
        return max_a

                    
        
