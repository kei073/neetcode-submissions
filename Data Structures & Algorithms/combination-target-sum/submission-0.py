class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        total = 0
        comb = []
        def dfs(i, total):
            if total > target:
                return
            if i == len(nums):
                if total == target:
                    res.append(comb.copy())
                return
            
            total += nums[i]
            comb.append(nums[i])
            dfs(i, total)
            total -= nums[i]
            comb.pop()

            dfs(i + 1, total)
        
        dfs(0, total=0)
        return res
