class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i, n1 in enumerate(nums):
            diff = target - n1
            if diff not in s:
                continue
            if n1 == diff and nums.count(n1) < 2:
                continue
            j = nums[i+1:].index(diff) + i + 1
            return [i, j]