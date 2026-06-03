class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1):
            for left in range(n):
                right = left + length - 1
                if right >= n:
                    continue
                
                if s[left] == s[right] and \
                   (length == 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

        res = 0
        for left in range(n):
            for right in range(left, n):
                res += dp[left][right]
        return res