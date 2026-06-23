class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sắp xếp theo điểm kết thúc
        intervals.sort(key=lambda x: x[1])
        
        # Chỉ cần lưu điểm kết thúc của khoảng hợp lệ gần nhất
        end = intervals[0][1]
        res = 0
        
        for i in range(1, len(intervals)):
            # Nếu khoảng tiếp theo bắt đầu TRƯỚC khi khoảng cũ kết thúc -> Chồng chéo
            if intervals[i][0] < end:
                res += 1
            else:
                # Không chồng chéo -> Cập nhật điểm kết thúc mới
                end = intervals[i][1]
                
        return res