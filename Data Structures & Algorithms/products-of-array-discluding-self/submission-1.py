class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [1] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i]
        
        suff = [1] * n
        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        
        res = []
        for i in range(n):
            val = 1
            if 0 <= i - 1:
                val *= pref[i - 1]
            if i + 1 <= n - 1:
                val *= suff[i + 1]
            
            res.append(val)

        return res