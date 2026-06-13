from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(lambda: 1) # {(slope, b): npts, (slope, b): npts, ...}
        mx = 1
        for i, (x2, y2) in enumerate(points):
            seen = set()
            for j in range(i):
                x1, y1 = points[j]
                dy, dx = y2-y1, x2-x1
                slope = dy/dx if dx != 0 else None
                b = y1 - slope*x1 if slope is not None else x1
                line = (slope, b)
                if line in seen:
                    continue
                seen.add(line)
                lines[line] += 1
                if lines[line] > mx:
                    mx = lines[line]
        return mx