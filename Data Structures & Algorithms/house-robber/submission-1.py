class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [[0] * 2 for _ in range(n)]

        dp[0][0], dp[0][1] = 0, nums[0]
        dp[1][0], dp[1][1] = max(dp[0]), nums[1]

        for i in range(2, n):
            dp[i][0] = max(dp[i][0], max(dp[i - 1]))
            dp[i][1] = max(dp[i][1], max(dp[i - 2]) + nums[i])
        
        return max(dp[n - 1])