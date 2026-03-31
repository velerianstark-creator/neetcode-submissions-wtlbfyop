class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = self.convert(s1)
        l = 0
        k = len(s1)
        while l + k - 1 < len(s2):
            if set1 == self.convert(s2[l : l + k]):
                return True
            else:
                l += 1
        return False

    def convert(self, s: str):
        my_map = {}
        my_set = set()
        for ch in s:
            if ch in my_map:
                my_map[ch] += 1
            else:
                my_map[ch] = 1
        for k, v in my_map.items():
            my_set.add(str(v) + k)
        return my_set
        