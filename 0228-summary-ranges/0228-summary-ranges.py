class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            a = nums[i]
            while i < len(nums)-1 and nums[i+1] == nums[i]+1:
                i += 1
            if nums[i] == a:
                res.append(f"{a}")
            else:
                res.append(f"{a}->{nums[i]}")
            i += 1
        
        return res
        