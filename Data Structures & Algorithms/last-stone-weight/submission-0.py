from heapq import heapify, heappush, heappop
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [- stone for stone in stones]
        heapq.heapify(stones)
        while len(stones):
            first = heappop(stones)
            if not stones:
                return - first
            second = heappop(stones)
            remain =  first - second
            if remain:
                heappush(stones, remain)

        return 0