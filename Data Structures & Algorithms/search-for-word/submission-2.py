class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # num_row, num_col = len(board), len(board[0])
        def backtrack(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[index]:
                return False
            temp = board[row][col]
            board[row][col] = "#"
            result = backtrack(row + 1, col, index + 1) or backtrack(row, col + 1, index + 1) or backtrack(row - 1, col, index + 1) or backtrack(row, col - 1, index + 1)   
            board[row][col] = temp
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False