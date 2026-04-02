import operator
from collections import deque
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = deque()
        for i in range(len(tokens)):
            try:
                stack.append(float(tokens[i]))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(ops[tokens[i]](a, b)))
                   
        if len(stack) != 1:
            return None
            
        return int(stack.pop())
        