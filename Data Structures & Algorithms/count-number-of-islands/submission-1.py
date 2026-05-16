class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            backtrack(row - 1, col)
            backtrack(row + 1, col)
            backtrack(row, col - 1)
            backtrack(row, col + 1)

        numb = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numb += 1
                    backtrack(i,j)
        return numb