class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if i - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (text1[i] == text2[j]))
                else:
                    dp[i][j] = max(dp[i][j], int(text1[i] == text2[j]))
        
        return dp[-1][-1]