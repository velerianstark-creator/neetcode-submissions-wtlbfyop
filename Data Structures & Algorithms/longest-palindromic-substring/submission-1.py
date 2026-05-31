class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "#" + '#'.join(s) + "#"
        n = len(T)
        P = [0] * n
        R = 0
        C = 0
        for i in range(1, n - 1):
            if i <= R:
                P[i] = min(R - i, P[2 * C - i])
            while True:
                if i - 1 - P[i] < 0 or i + 1 + P[i] >= n:
                    break
                if T[i - 1 - P[i]] != T[i + 1 + P[i]]:
                    break
                P[i] += 1
            if i + P[i] >= R:
                C = i
                R = i + P[i]
        r_max, c_max = 0, 0
        for i in range(len(P)):
            if P[i] > r_max:
                r_max = P[i]
                c_max = i
        return s[(c_max - r_max)//2: (c_max - r_max)//2 + r_max]
