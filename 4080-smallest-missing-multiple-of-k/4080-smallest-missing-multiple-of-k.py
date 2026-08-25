class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)
        for i in range(1, len(nums)+2):
            if i*k not in numsSet:
                return i*k