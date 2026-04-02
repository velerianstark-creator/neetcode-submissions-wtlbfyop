from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        dq = deque(temperatures)
        # result = 0
        i = 1
        while i < len(dq):
            if dq[0] >= dq[i]: 
                if i == len(dq) - 1:
                    res.append(0)
                    dq.popleft()
                    i = 1
                else:
                    i += 1
            else:
                res.append(i)
                dq.popleft()
                i = 1
        if len(temperatures) > 0:
            res.append(0)
        return res      