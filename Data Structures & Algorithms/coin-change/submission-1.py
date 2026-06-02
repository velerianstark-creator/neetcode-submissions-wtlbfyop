class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def getCoinNum(rem):
            res = float('inf')
            if rem == 0:
                return 0
            if rem < 0:
                return - 1
            if rem in memo:
                return memo[rem]
            min_coins = float('inf')
            for coin in coins:
                if rem >= coin:
                    res = getCoinNum(rem - coin)
                if res >= 0:
                    min_coins = min(min_coins, res + 1)
            memo[rem] = min_coins if min_coins != float('inf') else -1
            return memo[rem]
        return getCoinNum(amount)
                