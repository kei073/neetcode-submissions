class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSub = nums[0], nums[0]

        for num in nums[1:]:
            curSum = max(num, num + curSum)
            maxSub = max(maxSub, curSum)
        
        return maxSub