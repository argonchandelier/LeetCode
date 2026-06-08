class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while r-l > 3:
            c = (l+r)//2
            L, C, R = nums[l], nums[c], nums[r]
            if L <= C <= R:
                l = c
            elif R <= C <= L:
                r = c
            elif C <= L and C <= R:
                r = c
            else: # C highest
                l2 = (l+c)//2
                L2 = nums[l2]
                if L2 >= C:
                    r = c
                else:
                    l = l2
        final = [float('-inf') if l == 0 else nums[l-1]] + nums[l:r+1] + [float('-inf') if r+1 == n else nums[r+1]]
        print(final)
        for i in range(1, len(final)-1):
            if final[i-1] < final[i] and final[i+1] < final[i]:
                return l+i-1
        
        return -2
