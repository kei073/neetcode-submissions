class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        bit = -1
        for x in range(1, n + 1):
            if (x == 1 << (bit + 1)):
                bit += 1
            res[x] += res[x - (1 << bit)] + 1

        return res