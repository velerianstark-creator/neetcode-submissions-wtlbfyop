class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for current in intervals[1:]:
            if res[-1][1] < current[0]:
                res.append(current)
            else:
                res[-1][1] = max(res[-1][1], current[1])
        return res