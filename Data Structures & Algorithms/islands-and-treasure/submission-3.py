from collections import deque
import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # def backtrack(x, y, current):

        #     if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        #         return
        #     if grid[x][y] == -1: 
        #         return
        #     if grid[x][y] == 0 and current != 0:
        #         return
        #     temp = grid[x][y]
        #     if grid[x][y] > current:
        #         temp = current
        #     grid[x][y] = -1
        #     backtrack(x+1, y, current + 1)
        #     backtrack(x-1, y, current + 1)
        #     backtrack(x, y +1, current + 1)
        #     backtrack(x, y - 1, current + 1)
        #     grid[x][y] = temp
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j , 0])
        while queue:
            pos = queue.popleft()
            i = pos[0]
            j = pos[1]
            current = pos[2]
            if grid[i][j] > current:
                grid[i][j] = current
            if i - 1 >= 0 and grid[i-1][j] > pos[2] + 1:
                grid[i -1][j] = pos[2] + 1
                queue.append([i-1,j, pos[2] + 1])
            if i + 1 < len(grid) and grid[i+1][j] > pos[2] + 1:
                grid[i+1][j] = pos[2] + 1
                queue.append([i+1,j, pos[2] + 1])            
            if j - 1 >= 0 and grid[i][j-1] > pos[2] + 1:
                grid[i][j-1] = pos[2] + 1
                queue.append([i,j-1, pos[2] + 1])
            if j + 1 < len(grid[0]) and grid[i][j+1] > pos[2] + 1:
                grid[i][j+1] = pos[2] + 1
                queue.append([i,j+1, pos[2] + 1])                