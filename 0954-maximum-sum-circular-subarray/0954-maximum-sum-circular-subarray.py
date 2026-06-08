class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        minsum = maxsum
        mx, mn = maxsum, minsum

        for i, num in enumerate(nums[1:], start=1):
            maxsum += num
            minsum += num
            if num > maxsum:
                maxsum = num
            if num < minsum:
                minsum = num

            mx, mn = max(maxsum, mx), min(minsum, mn)
        
        return max(mx, sum(nums)-mn) if mx > 0 else mx