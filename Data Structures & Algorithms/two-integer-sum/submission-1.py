class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # value -> index

        for j in range(len(nums)):
            diff = target - nums[j]

            if diff in indices:
                i = indices[diff]
                return [i, j]
            
            if nums[j] not in indices:
                indices[nums[j]] = j
    
