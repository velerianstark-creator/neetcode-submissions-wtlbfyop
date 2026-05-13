class KthLargest:
    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
       

    def add(self, val: int) -> int:
        if len(self.nums) + 1>= self.k:
            self.nums.append(val)
            self.nums.sort()
            return self.nums[len(self.nums) - self.k]
        return
