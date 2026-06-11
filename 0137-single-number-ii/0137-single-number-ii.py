class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        superbits = [0]*32
        for num in nums:
            i = 0
            num &= 0xffffffff
            while num:
                superbits[i] = (superbits[i] + (num&1)) % 3
                num = num >> 1
                i += 1
        res = 0
        for bit in superbits[::-1]:
            res = (res << 1) | bit
        return res if superbits[31] == 0 else res - 2**32

