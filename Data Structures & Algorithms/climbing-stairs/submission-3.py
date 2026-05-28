class Solution:
    def climbStairs(self, n: int) -> int:
        def backtrack(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if memo.get(i, 0):
                return memo[i]
            memo[i] = backtrack(i-1) + backtrack(i-2)
            return memo[i]
            
        memo = dict()
        return backtrack(n)