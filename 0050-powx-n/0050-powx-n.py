class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        sign = 1 if x >= 0 or n&1 == 0 else -1
        x = abs(x)
        if x in {0, 1}:
            return sign*x
        nsign = 1 if n > 0 else -1
        n *= nsign
        
        stored = [1]*n.bit_length()
        cur = x
        for i in range(n.bit_length()):
            if n&1 == 1:
                stored[i] = cur
            cur *= cur
            n = n >> 1
        res = 1
        for st in stored:
            res *= st
        res *= sign
        return res if nsign == 1 else 1./float(res)
        



        