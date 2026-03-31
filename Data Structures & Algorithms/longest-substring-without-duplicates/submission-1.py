class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        seen = set()
        # seen.add(s[0])
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                for k in range(l, r):
                    if s[k] == s[r]:
                        seen.remove(s[r])
                        l = k + 1
                        break
                    else:
                        seen.remove(s[k])    
        return res
        