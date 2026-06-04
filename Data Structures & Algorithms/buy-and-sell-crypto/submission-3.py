class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        curMin = prices[0]
        for i in range(len(prices)):
            res = max(res, prices[i] - curMin)
            curMin = min(curMin, prices[i])
        
        return res