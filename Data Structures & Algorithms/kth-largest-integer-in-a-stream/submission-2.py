class KthLargest:
    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
       

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums = []
        self.nums.append(val)
        if len(self.nums)>= self.k:
            self.nums.sort()
            return self.nums[len(self.nums) - self.k]
        return
