class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [0]*n
        bwd = [0]*n
        fwd[0] = nums[0]
        bwd[-1] = nums[-1]
        for i in range(1, n):
            fwd[i] = fwd[i-1]*nums[i]
            bwd[-i-1] = bwd[-i]*nums[-i-1]
        full = [0]*n
        full[0], full[-1] = bwd[1], fwd[-2]
        for i in range(1, n-1):
            full[i] = fwd[i-1]*bwd[i+1]
        return full
