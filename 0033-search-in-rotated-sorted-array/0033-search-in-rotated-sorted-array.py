class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            L, R = nums[l], nums[r]
            c = (l+r)//2
            C = nums[c]
            if C == target:
                return c
            if L < R:
                if C < target:
                    l = c+1
                else:
                    r = c-1
                continue
            if C >= L:
                if target > C or target < L:
                    l = c+1
                else:
                    r = c-1
                continue
            if target >= L or target < C:
                r = c-1
                continue
            l = c+1
        return -1
