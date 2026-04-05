class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumProdFromLeft = [1] * len(nums)
        cumProdFromLeft[0] = nums[0]
        for i in range(1, len(nums)):
            cumProdFromLeft[i] = cumProdFromLeft[i - 1] * nums[i]
        
        cumProdFromRight = [1] * len(nums)
        cumProdFromRight[0] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            cumProdFromRight[i] = cumProdFromRight[i - 1] * nums[len(nums) - 1 - i]
        
        res = []
        for i in range(len(nums)):
            val = 1
            if 0 <= i - 1:
                val *= cumProdFromLeft[i - 1]
            if i + 1 <= len(nums) - 1:
                val *= cumProdFromRight[len(nums) - 1 - (i + 1)]
            
            res.append(val)

        return res