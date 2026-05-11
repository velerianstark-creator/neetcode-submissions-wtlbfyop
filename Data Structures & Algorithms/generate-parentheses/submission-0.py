class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(i, o, c, current):
            if i == c:
                output.append(current)
                return
            if o > c:
                backtrack(i, o, c + 1, current + ")")
            if i > o:
                backtrack(i, o + 1, c, current + "(")
            
        output = []
        backtrack(n, 0, 0, "")
        return output