from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = deque(sorted(set(heights)))
        max_a = 0
        deque_h = deque(heights)

        while len(h) > 0:
            if h[0] == 0:
                h.popleft()
                continue
            if deque_h[0] < h[0]:
                deque_h.popleft()
                # h.popleft()
                continue
            j = 0
            i = 0
            while i + j < len(deque_h):
                if deque_h[i + j] >= h[0]:
                    j += 1
                    if i + j == len(deque_h):
                        max_a = max(max_a, h[0] * j)
                        break
                else:
                    max_a = max(max_a, h[0] * j)
                    i += j + 1
                    j = 0
            h.popleft()
        return max_a

                    
        
