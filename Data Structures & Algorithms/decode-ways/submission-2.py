class Solution:
    def numDecodings(self, s: str) -> int:
        def decode(i) -> int:
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            
            if int(s[i]) == 0:
                memo[i] = 0
                return 0
            if i == len(s) - 1:
                return 1
            res = decode(i+1)
            if int(s[i:i+2]) <= 26:
                res += decode(i+2)
            memo[i] = res
            return res
        memo = {}
        return decode(0)