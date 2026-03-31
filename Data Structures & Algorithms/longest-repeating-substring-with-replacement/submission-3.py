class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            while  k < r - l + 1 - max_freq:
                freq[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res