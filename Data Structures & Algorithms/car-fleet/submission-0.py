from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict_v = {}
        time = deque()
        n = len(position)
        l = 0
        r = 1
        res = n
        for i in range(n):
            dict_v[position[i]] = float((target -position[i])/speed[i])
        pos = sorted(position)
        for p in pos:
            time.append(dict_v[p])
        while r < len(time):
            if time[0] <= time[r]:
                for _ in range(r):
                    time.popleft()
                    res -= 1
                r = 1
            elif r == len(time) - 1:
                time.popleft()
                r = 1
            else:
                r += 1
        return res

            