class Solution:
    def trailingZeroes(self, n: int) -> int:
        div = 5
        res = 0
        while div <= n:
            res += n // div
            div *= 5
        return res