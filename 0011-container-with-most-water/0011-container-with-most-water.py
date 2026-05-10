class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1
        mxl, mxr = height[p1], height[p2]
        mxa = min(mxl, mxr)*(p2-p1)
        while p1 < p2:
            if mxl <= mxr:
                p1 += 1
                while height[p1] < mxl:
                    p1 += 1
                    if p1 == p2:
                        break
                mxl = height[p1]
            else:
                p2 -= 1
                while height[p2] < mxr:
                    p2 -= 1
                mxr = height[p2]
            mxa = max(mxa, min(mxl, mxr)*(p2-p1))
        
        return mxa
