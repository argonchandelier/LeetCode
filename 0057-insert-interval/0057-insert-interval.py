class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        n1, n2 = newInterval
        i = 0
        while intervals[i][1] < n1:
            i += 1
            if i == len(intervals):
                return intervals + [newInterval]
        a = min(n1, intervals[i][0])
        pa = i
        while n2 >= intervals[i][0]:
            i += 1
            if i == len(intervals):
                return intervals[:pa] + [[a, max(intervals[-1][1], n2)]]
        b = max(intervals[i-1][1], n2) if i > 0 else n2
        return intervals[:pa] + [[a, b]] + intervals[i:]
