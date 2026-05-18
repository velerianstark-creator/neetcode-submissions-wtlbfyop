from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    total += 1
                    if grid[row][col] == 2:
                        queue.append([row,col])
        time = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                rot = queue.popleft()
                if rot[0] - 1 >= 0 and grid[rot[0]-1][rot[1]] == 1:
                    grid[rot[0]-1][rot[1]] = 2
                    queue.append([rot[0]-1, rot[1]])
                if rot[0] + 1 < len(grid) and grid[rot[0]+1][rot[1]] == 1:
                    grid[rot[0]+1][rot[1]] = 2
                    queue.append([rot[0]+1, rot[1]])
                if rot[1] - 1 >= 0 and grid[rot[0]][rot[1]-1] == 1:
                    grid[rot[0]][rot[1]-1] = 2
                    queue.append([rot[0], rot[1]-1])
                if rot[1] + 1 < len(grid[0]) and grid[rot[0]][rot[1]+1] == 1:
                    grid[rot[0]][rot[1]+1] = 2
                    queue.append([rot[0], rot[1]+1])
            total -= size
            time += 1
        if total>0:
            return -1
        if time>0:
            return time
        return 0                                    

