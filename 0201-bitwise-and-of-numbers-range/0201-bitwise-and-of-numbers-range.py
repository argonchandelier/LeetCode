class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        if len(bin(left)) != len(bin(right)):
            return 0
        a, b = f"{left:b}", f"{right:b}"
        n = len(a)
        res = ['0']*n
        for i in range(n):
            if a[i] != b[i]:
                break
            res[i] = a[i]
        return int(''.join(res), 2)