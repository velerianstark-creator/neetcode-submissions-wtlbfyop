class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare = {}
        compare['('] = ')'
        compare['['] = ']'
        compare['{'] = '}'
        for ch in s:
            if ch in compare:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if compare[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        