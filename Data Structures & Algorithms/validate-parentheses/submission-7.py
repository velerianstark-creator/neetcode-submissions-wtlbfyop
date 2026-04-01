from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        compare =  { ")" : "(", "]" : "[", "}" : "{" }
        for ch in s:
            if ch not in compare:
                stack.append(ch)
            else:
                if stack and stack[-1] == compare[ch]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        