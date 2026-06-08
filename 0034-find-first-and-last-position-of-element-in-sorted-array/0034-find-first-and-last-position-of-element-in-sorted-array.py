class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tl, tr = -1, -1
        def bsearch(targ, nums):
            l, r = 0, len(nums)-1
            while l <= r:
                c = (l+r)//2
                if nums[c] < targ:
                    l = c+1
                elif nums[c] > targ:
                    r = c-1
                else:
                    return True, c
            return False, l
        res, index = bsearch(target, nums)
        if not res:
            return [-1, -1]
        tl = bsearch(target-0.5, nums[:index])[1]
        tr = bsearch(target+0.5, nums[index+1:])[1] + index

        return [tl, tr]
