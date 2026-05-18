from collections import deque
import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j])
        current = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pos = queue.popleft()
                i = pos[0]
                j = pos[1]
                if grid[i][j] < current:
                    continue
                grid[i][j] = current
                if i - 1 >= 0 and grid[i-1][j] > current + 1:
                    grid[i -1][j] = current + 1
                    queue.append([i-1,j])
                if i + 1 < len(grid) and grid[i+1][j] > current + 1:
                    grid[i+1][j] = current + 1
                    queue.append([i+1,j])            
                if j - 1 >= 0 and grid[i][j-1] > current + 1:
                    grid[i][j-1] = current + 1
                    queue.append([i,j-1])
                if j + 1 < len(grid[0]) and grid[i][j+1] > current + 1:
                    grid[i][j+1] = current + 1
                    queue.append([i,j+1])   
            current += 1             