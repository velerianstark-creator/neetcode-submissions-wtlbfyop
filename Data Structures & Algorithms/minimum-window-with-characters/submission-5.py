class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        dict_s = {}
        res =""
        count = 0
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1
        length = len(dict_t)
        l = 0
        r = 0
        while r < len(s):
            if s[r] in dict_t:
                dict_s[s[r]] = dict_s.get(s[r], 0) + 1
                if dict_s[s[r]] == dict_t[s[r]]:
                    count += 1
                

                while l <= r and count == length:
                    if len(res) > r - l + 1 or res == "":
                        res = s[l : r + 1]
                    if s[l] in dict_t:
                        dict_s[s[l]] -= 1
                        if dict_s[s[l]] < dict_t[s[l]]:
                            count -= 1
                            # break
                    l += 1
            r += 1
        return res



            