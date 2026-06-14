from bisect import bisect_left as bl

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = nums[:1]
        for num in nums[1:]:
            i = bl(tails, num)
            if i == len(tails):
                tails.append(num)
                continue
            tails[i] = num
        return len(tails)
