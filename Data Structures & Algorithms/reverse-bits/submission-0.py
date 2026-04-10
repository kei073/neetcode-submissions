class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for power in range(32):
            bit = (n >> power) & 1
            res += bit << (31 - power)
        
        return res