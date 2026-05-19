import math
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def to_island(row, col, prev, visited):
            if (row, col) in visited:
                return
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
                return
            if heights[row][col] < prev:
                return
            visited.add((row, col))
            to_island(row +1, col, heights[row][col], visited) 
            to_island(row-1, col, heights[row][col], visited)
            to_island(row, col+1, heights[row][col], visited)
            to_island(row, col-1, heights[row][col], visited)
            
        visited_p = set()
        visited_a = set()
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    to_island(row, col, 0, visited_p)
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    to_island(row, col, 0, visited_a)
        output = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in visited_p and (row, col) in visited_a:
                    output.append([row, col])
        return output