class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Khởi tạo giá trị ban đầu tại phần tử đầu tiên
        max_so_far = nums[0]
        min_so_far = nums[0]
        global_max = nums[0] # Biến này để lưu kết quả lớn nhất lịch sử
        
        # Chạy từ phần tử thứ 2 trở đi
        for i in range(1, len(nums)):
            current = nums[i]
            
            # Giữ lại max_so_far cũ trước khi bị cập nhật
            temp_max = max_so_far 
            
            # Cập nhật max_so_far và min_so_far mới từ 3 ứng cử viên
            max_so_far = max(current, temp_max * current, min_so_far * current)
            min_so_far = min(current, temp_max * current, min_so_far * current)
            
            # Cập nhật kết quả lớn nhất tìm được từ trước đến nay
            global_max = max(global_max, max_so_far)
            
        return global_max