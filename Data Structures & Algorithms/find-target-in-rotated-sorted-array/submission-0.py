class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search 1: Find the pivot
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            pivot = 0
        else:
            while r - l > 1:
                m = (l + r) // 2

                if nums[l] <= nums[m]:
                    l = m
                elif nums[m] <= nums[r]:
                    r = m
            
            pivot = r
        
        # Binary Search 2
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            rl = (l + pivot) % len(nums)
            rr = (r + pivot) % len(nums)
            rm = (m + pivot) % len(nums)

            if nums[rm] == target:
                return rm
            elif target < nums[rm]:
                r = m - 1
            elif nums[rm] < target:
                l = m + 1
        
        return -1
