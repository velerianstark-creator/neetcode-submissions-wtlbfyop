class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(index, current):
            if index == len(digits):
                output.append(current)
                return
            btn = int(digits[index])
            for ch in source[btn-2]:
                backtrack(index + 1, current + ch)
                # current.pop()
        if len(digits) == 0:
            return []
        source = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        output = []
        backtrack(0, "")
        return output
