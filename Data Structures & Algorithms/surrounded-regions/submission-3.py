class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def from_border(x, y):
            if (x, y) in not_surround:
                return
            if x < 0 or y< 0 or x>= len(board) or y >= len(board[0]):
                return
            if board[x][y] == "X":
                return
            not_surround.add((x,y))
            from_border(x+1, y)
            from_border(x-1, y)
            from_border(x, y+1)
            from_border(x, y-1)

        not_surround = set()
        for i in range(len(board)):
            from_border(i, 0)
            from_border(i, len(board[0])-1)
        for j in range(len(board[0])):
            from_border(0, j)
            from_border(len(board)-1, j)
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == "O" and ((i,j) not in not_surround):
                    board[i][j] = "X"
