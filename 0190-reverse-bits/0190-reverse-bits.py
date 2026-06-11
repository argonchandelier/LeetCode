class Solution:
    def reverseBits(self, n: int) -> int:
        x = f"{n:b}"
        return int(x[::-1], 2)*2**(32-len(x))