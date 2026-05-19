from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def trace(queue, visited):
            while queue:
                size = len(queue)
                for _ in range(size):
                    island = queue.pop()
                    r = island[0]
                    c = island[1]
                    if (r, c) in visited:
                        continue
                    if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                        queue.append([r-1, c])
                    if r + 1 < len(heights) and heights[r+1][c] >= heights[r][c]:
                        queue.append([r+1, c])
                    if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                        queue.append([r, c-1])
                    if c + 1 < len(heights[0]) and heights[r][c+1] >= heights[r][c]:
                        queue.append([r, c+1])
                    visited.add((island[0], island[1]))
        queue_p = deque()
        queue_a = deque()
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    queue_p.append([row, col])
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    queue_a.append([row, col])
        # memo_p = [[False] * len(heights[0]) for _ in range(len(heights))]
        # memo_a = [[False] * len(heights[0]) for _ in range(len(heights))]
        visited_p = set()
        visited_a = set()
        trace(queue_p, visited_p)
        trace(queue_a, visited_a)
        output = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in visited_p and (row, col) in visited_a:
                    output.append([row, col])
        return output
