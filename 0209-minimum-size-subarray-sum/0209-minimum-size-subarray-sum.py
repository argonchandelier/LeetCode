class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        mn = float('inf')
        p1, p2 = 0, 0
        cur = 0
        while p2 < n:
            cur += nums[p2]
            if cur < target:
                p2 += 1
                if p2-p1 >= mn:
                    cur -= nums[p1]
                    p1 += 1
                continue
            while cur >= target:
                cur -= nums[p1]
                p1 += 1
            mn = min(mn, p2-p1+2)
            p2 += 1
        
        return mn if mn < float('inf') else 0