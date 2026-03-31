class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        n = len(nums)
        bucket = {}
        result = []
        for num in nums:
            if num in my_map:
                my_map[num] += 1
            else:
                my_map[num] = 1
        for key in my_map:
            bucket.setdefault(my_map[key], []).append(key)
        for j in range(n, 0, -1):
            if j in bucket:
                result += bucket[j]
                if len(result) >= k:
                    return result