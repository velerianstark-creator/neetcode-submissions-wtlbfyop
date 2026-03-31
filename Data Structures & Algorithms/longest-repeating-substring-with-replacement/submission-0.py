class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        res = 0

        c = ''
        l = 0
        r = 0
        if len(s) <= k:
            return len(s)
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 1)
            max_freq = max(freq.values())

            if max_freq + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(r - l + 1, res)
                r += 1
                if r < len(s):
                    freq[s[r]] = freq.get(s[r], 0) + 1
                
        return res