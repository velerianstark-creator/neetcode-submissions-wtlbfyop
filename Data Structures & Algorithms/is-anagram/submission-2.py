class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = {}
        counter2 = {}
        for ch1 in s:
            if ch1 not in counter1:
                counter1[ch1] = 0
            else: counter1[ch1] += 1
        for ch2 in t:
            if ch2 not in counter2:
                counter2[ch2] = 0
            else: counter2[ch2] += 1
        return counter1 == counter2




        