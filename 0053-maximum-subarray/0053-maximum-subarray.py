class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        best = csum
        for num in nums[1:]:
            csum = num + max(0, csum)
            best = max(best, csum)

        return best