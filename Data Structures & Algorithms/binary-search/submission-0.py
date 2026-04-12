class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n,l,r = len(nums),0,len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        if l < n and nums[l] == target:
            return l
        return -1

        