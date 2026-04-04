from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = defaultdict(bool)
        for num in nums:
            if appeared[num]:
                return True
            appeared[num] = True
        return False