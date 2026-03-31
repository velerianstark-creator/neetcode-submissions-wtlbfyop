class Solution:
    import math
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map = {i: [] for i in range(1, 10, 1)}
        for j in range(9):
            for k in range(9):
                if board[j][k] != ".":
                    num = int(board[j][k])
                    cube = (j // 3) * 3 + k // 3
                    pos = [cube, j, k]
                    if (map[num] != []):
                        for ele in map[num]:
                            for i in range(3):
                                if ele[i] == pos[i]:
                                    return False
                    map[num].append(pos)
        return True