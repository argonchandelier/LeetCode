class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        vertical = [[0]*n for _ in range(m)]
        horizontal = [[0]*n for _ in range(m)]
        matrix = [[int(matrix[r][c]) for c in range(n)] for r in range(m)]
        mx = 0
        if matrix[0][0] == 1:
            horizontal[0][0] = 1
            vertical[0][0] = 1
            mx = 1
        for r in range(1, m):
            if matrix[r][0] == 0:
                continue
            vertical[r][0] = vertical[r-1][0] + 1
            horizontal[r][0] = 1
            mx = 1
        for c in range(1, n):
            if matrix[0][c] == 0:
                continue
            horizontal[0][c] = horizontal[0][c-1] + 1
            vertical[0][c] = 1
            mx = 1

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    continue
                lr, lc = r-1, c-1
                lv, lh = vertical[lr][c], horizontal[r][lc]
                vertical[r][c] = 1 + lv
                horizontal[r][c] = 1 + lh
                val = 1 + min(lv, lh, matrix[lr][lc])
                matrix[r][c] = val
                if val > mx:
                    mx = val
        print(horizontal)
        print(vertical)
        print(matrix)
        return mx*mx

