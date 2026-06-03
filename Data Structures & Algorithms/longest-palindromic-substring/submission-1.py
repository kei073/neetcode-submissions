class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1
        
        for length in range(2, n + 1):
            for left in range(n):
                right = left + length - 1
                if right >= n:
                    continue
                
                if s[left] == s[right] and \
                   (length == 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    
                    if max_len < length:
                        start = left
                        max_len = length
        
        return s[start:start + max_len]