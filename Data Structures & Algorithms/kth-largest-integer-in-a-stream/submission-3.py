class KthLargest:
    def __init__(self, k: int, nums: List[int]):

        self.k = k
        if nums:
            self.nums = nums
        else:
            self.nums = []
       

    def add(self, val: int) -> int:
        self.nums.append(val)
        if len(self.nums)>= self.k:
            self.nums.sort()
            return self.nums[len(self.nums) - self.k]
        return
