class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        res = 0
        while i < len(points):
            x1, x2 = points[i]
            i += 1
            while i < len(points) and x2 >= points[i][0]:
                x2 = min(x2, points[i][1])
                i += 1
            res += 1
        
        return res