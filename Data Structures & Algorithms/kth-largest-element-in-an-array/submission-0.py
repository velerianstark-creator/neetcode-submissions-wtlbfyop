from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)