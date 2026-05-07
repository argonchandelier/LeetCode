class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        backmax = [0]*(n+1)
        mx = 0
        for i in range(n-1, -1, -1):
            h = height[i]
            if h > mx:
                mx = h
            backmax[i] = mx
        
        mx = 0
        res = 0
        for i, h in enumerate(height):
            add = min(mx, backmax[i+1]) - h
            if add > 0:
                res += add
            if h > mx:
                mx = h
        
        return res