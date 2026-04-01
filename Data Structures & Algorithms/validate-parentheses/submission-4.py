class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare = {}
        compare['('] = ')'
        compare['['] = ']'
        compare['{'] = '}'
        for i in range(0, len(s)):
            if s[i] in compare:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif compare[stack[- 1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        