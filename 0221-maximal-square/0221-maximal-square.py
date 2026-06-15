class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        matrix = [[int(matrix[r][c]) for c in range(n)] for r in range(m)]
        mx = int(any(x == 1 for x in matrix[0]) or any(row[0] == 1 for row in matrix))
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    continue
                lr, lc = r-1, c-1
                val = 1 + min(matrix[lr][c], matrix[r][lc], matrix[lr][lc])
                matrix[r][c] = val
                if val > mx:
                    mx = val
        return mx*mx

