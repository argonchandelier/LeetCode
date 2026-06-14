class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for c in range(1, m+n-1):
            i, j = c, 0
            if i >= m:
                over = i-m+1
                i, j = m-1, over
            while i >= 0 and j < n:
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                i -= 1
                j += 1
        return grid[-1][-1]
            