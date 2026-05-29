class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = [0, 0]
        for n in range(len(cost)+1):
            if n == 0:
                continue
            if n == 1:
                continue
            twoStep = store[0] + cost[n-2]
            oneStep = store[1] + cost[n-1]
            store[0] = store[1]
            store[1] = min(oneStep, twoStep)
        return store[1]