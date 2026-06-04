class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total % 2:
            return False
        n = len(nums)
        half = total//2
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            for j in range(half, num - 1, -1): 
                if dp[j - num]:
                    dp[j] = True
        return dp[half]
                # Duyệt lùi các tổng từ half về num
        # NẾU tổng j - num trước đó ĐÃ tạo được (tức là True)
        # THÌ tổng j hiện tại cũng sẽ tạo được bằng cách cộng thêm num vào!

                    