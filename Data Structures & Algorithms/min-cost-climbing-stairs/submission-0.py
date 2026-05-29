class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def checkMin(n):
            if n == 0:
                return 0
            if n == 1:
                return 0
            twoStep = store[0] + cost[n-2]
            oneStep = store[1] + cost[n-1]
            store[0] = store[1]
            store[1] = min(oneStep, twoStep)

        store = [0, 0]
        for i in range(len(cost)+1):
            checkMin(i)
        return store[1]