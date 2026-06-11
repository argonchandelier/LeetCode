class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        n = x.bit_length()
        nr = 2**((n+1)//2)
        r = nr+1
        while nr < r:
            r = nr
            nr = (r + x//r) // 2
        return r