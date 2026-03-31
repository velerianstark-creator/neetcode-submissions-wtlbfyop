class Solution:
    def trap(self, height: List[int]) -> int:

        # area = 0
        # i = 0
        # while height and height[0] == 0:
        #     height.pop(0)
        # while height and height[-1] == 0:
        #     height.pop()
        length = len(height)
        if length <= 2:
            return 0
        l, r, i, j, area = 0, length -1, 1, 1, 0
        while (l < r):
            if height[l] <= height[r]:
                if height[l] > height[l+i]:
                    area += height[l] - height[l+i]
                    i += 1
                else:
                    l += i
                    i = 1
            else:
                if height[r] > height[r-j]:
                     area += height[r] - height[r - j]
                     j += 1
                else:
                    r -= j
                    j = 1    
        return area            
                