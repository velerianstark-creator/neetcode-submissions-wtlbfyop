class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandFromCenter(s: str, left: int, right: int) -> int:
            count = 0
            while left >= 0 and right <len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
            return count
        total_count = 0
        for i in range(len(s)):
            # 1. Gọi hàm expandFromCenter cho TÂM LẺ tại vị trí i
            total_count += expandFromCenter(s, i, i)
            # 2. Gọi hàm expandFromCenter cho TÂM CHẴN tại vị trí i và i+1
            total_count += expandFromCenter(s, i, i + 1)           
        return total_count