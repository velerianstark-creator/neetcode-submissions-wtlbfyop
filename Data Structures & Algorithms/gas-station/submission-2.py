class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        balance = 0
        rem = 0
        for i in range(n):
            balance += gas[i] - cost[i]
        if balance < 0:
            return - 1
        for i in range(n):
            rem += gas[i] - cost[i]
            if rem < 0:
                start = i+1
                rem = 0
        if start >= n:
            return -1
        return start
        