class Solution:
    def uniquePathsWithObstacles(self, ogrid: List[List[int]]) -> int:
        if ogrid[-1][-1] == 1 or ogrid[0][0] == 1:
            return 0
        m, n = len(ogrid), len(ogrid[0])
        grid = [[-1 if val == 1 else 0 for val in row] for row in ogrid]
        grid[0][0] = 1
        for c in range(1, n):
            if grid[0][c] == -1:
                break
            grid[0][c] = grid[0][c-1]
        for r, row in enumerate(grid[1:], start=1):
            rp = r-1
            if grid[rp][0] > 0 and grid[r][0] > -1:
                grid[r][0] = 1
            for c in range(1, n):
                if grid[r][c] == -1:
                    continue
                cp = c-1
                if grid[rp][c] > 0:
                    grid[r][c] = grid[rp][c]
                if grid[r][cp] > 0:
                    grid[r][c] += grid[r][cp]
        return grid[-1][-1]
