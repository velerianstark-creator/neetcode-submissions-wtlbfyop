class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def backtrack(row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if not grid[row][col]:
                return
            area[0] += 1
            grid[row][col] = 0
            backtrack(row - 1, col)
            backtrack(row + 1, col)
            backtrack(row, col - 1)
            backtrack(row, col + 1)
            

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = [0]
                if grid[i][j]:
                    backtrack(i,j)
                    max_area = max(area[0], max_area)
        return max_area