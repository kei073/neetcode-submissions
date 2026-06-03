class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        
        for length in range(1, n):
            for left in range(1, n):
                right = left + length - 1
                if right >= n - 1:
                    continue
                
                dp[left - 1][right + 1] |= dp[left][right] and (s[left - 1] == s[right + 1])

        max_length = 0
        ans = ""
        for left in range(n):
            for right in range(n):
                length = right - left + 1
                if dp[left][right] and max_length < length:
                    max_length = length
                    ans = s[left:right+1]
        
        return ans