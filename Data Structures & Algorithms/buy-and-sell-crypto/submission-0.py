class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        i = 0
        j = 1
        while i + j < length:
            if (prices[i] < prices[i +j]):
                max_profit = max(max_profit, prices[i +j] - prices[i])
                j += 1
            else:
                i += j
                j = 1
        return max_profit


        