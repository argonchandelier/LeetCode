from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        nislands = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == '0':
                    continue
                nislands += 1
                q = deque([(r, c)])
                while q:
                    r1, c1 = q.popleft()
                    for dr, dc in ((0,1), (1,0), (0,-1), (-1, 0)):
                        r2, c2 = r1+dr, c1+dc
                        if not (0 <= r2 < m) or not (0 <= c2 < n) or grid[r2][c2] == '0':
                            continue
                        grid[r2][c2] = '0'
                        q.append((r2, c2))
        return nislands