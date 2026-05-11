class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n, open_amount, close_amount, current):
            if close_amount == n:
                output.append(current)
                return
            if open_amount < n:
                backtrack(n, open_amount + 1, close_amount, current + "(")
            if open_amount > close_amount:
                backtrack(n, open_amount, close_amount + 1, current + ")")

            
        output = []
        backtrack(n, 0, 0, "")
        return output