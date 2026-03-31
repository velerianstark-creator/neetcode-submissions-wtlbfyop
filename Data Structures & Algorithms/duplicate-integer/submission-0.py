class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            len_before = len(hash_set)
            hash_set.add(num)
            len_after = len(hash_set)
            if len_before == len_after:
                return True
        return False
            

