class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if self.binary_search(nums, target, left=j + 1, right=len(nums) - 1):
                    triplet = [nums[i], nums[j], target]
                    if triplet not in res:
                        res.append(triplet)
        
        return res


    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        
        return False
                
