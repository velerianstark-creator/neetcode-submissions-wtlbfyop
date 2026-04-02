import operator
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        digit = []
        i = 0
        while len(tokens) > 1:
            try:
                tokens[i] = float(tokens[i])
                i += 1
            except ValueError:
                tokens[i - 2] = int(ops[tokens[i]](tokens[i - 2], tokens[i - 1]))
                tokens.pop(i)
                tokens.pop(i - 1)
                i -= 1      
        if len(tokens) != 1:
            return None
            
        return int(tokens[0])
        