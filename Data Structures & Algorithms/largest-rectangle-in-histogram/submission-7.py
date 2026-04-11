class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        width = 0
        n = len(heights)
        for i in range(n):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                if len(stack) > 0:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, width * heights[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            max_area = max(max_area, width * heights[j])
            
        return max_area
