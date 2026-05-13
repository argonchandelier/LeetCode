class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            a, b = intervals[i]
            while i < len(intervals)-1 and intervals[i+1][0] <= b:
                i += 1
                b = max(b, intervals[i][1])
            res.append([a, b])
            i += 1
        
        return res