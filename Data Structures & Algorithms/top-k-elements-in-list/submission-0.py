from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        val_key_pair = [(val, key) for key, val in counter.items()]
        val_key_pair.sort(reverse=True)

        res = []
        for i, (val, key) in enumerate(val_key_pair[:k]):
            res.append(key)
        
        return res