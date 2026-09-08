class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        mx, mins = nums[0], [nums[-1]]*l
        for i in range(1,l):
            mins[-i-1] = mins[-i] if nums[-i-1] > mins[-i] else nums[-i-1]
        for i in range(l):
            mx = max(nums[i], mx)
            if mx - mins[i] <= k:
                return i
        return -1