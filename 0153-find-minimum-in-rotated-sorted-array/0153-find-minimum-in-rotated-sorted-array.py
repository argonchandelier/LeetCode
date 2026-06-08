class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        L, R = nums[l], nums[r]
        while True:
            c = (l+r)//2
            L, C, R = nums[l], nums[c], nums[r]
            if L <= R:
                return L
            if C >= L:
                l = c+1
            else:
                r = c