class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(index, current):
            if index == len(s):
                output.append(current.copy())
            for j in range(index, len(s)):
                if isPalindrome(s[index: j + 1]):
                    current.append(s[index: j+1])
                    backtrack(j + 1, current)
                    current.pop()
        def isPalindrome(subString):
            left = 0
            right = len(subString) - 1
            while left < right:
                if subString[left] != subString[right]:
                    return False
                left += 1
                right -= 1
            return True
        output = []
        backtrack(0, [])
        return output
