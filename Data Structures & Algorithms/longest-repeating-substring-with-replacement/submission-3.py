class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            maxf = self.maxFrequency(count)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                maxf = self.maxFrequency(count)
            res = max(res, r - l + 1)
        
        return res
    
    def maxFrequency(self, d: dict) -> int:
        return max(d.values())
            