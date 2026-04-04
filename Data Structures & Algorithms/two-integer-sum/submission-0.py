class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # seen[value] = index
        for j in range(len(nums)):
            x = target - nums[j]  # nums[i]
            if x in seen:
                i = seen[x]
                return [i, j]
            if nums[j] not in seen:
                seen[nums[j]] = j
    
