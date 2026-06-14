class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for c in range(1, m+n-1):
            i, j = c, 0
            if i >= m:
                over = i-m+1
                i, j = m-1, over
            while i >= 0 and j < n:
                grid[i][j] += min((grid[i][j-1] if j > 0 else float('inf')), (grid[i-1][j] if i > 0 else float('inf')))
                i -= 1
                j += 1
        return grid[-1][-1]
            