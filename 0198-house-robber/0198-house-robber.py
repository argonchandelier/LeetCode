class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0]*len(nums)
        dp[:2] = nums[:2]
        dp[2] = max(dp[1], dp[0]+nums[2])
        for i, num in enumerate(nums[3:], start=3):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i])
        return max(dp[-2:])

            
        
