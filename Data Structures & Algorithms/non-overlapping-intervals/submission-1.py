class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        interval = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if interval[1] <= intervals[i][0]:
                interval = intervals[i]
                continue
            else:
                res += 1
        return res