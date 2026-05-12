class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        r0 = 0 in matrix[0]
        c0 = False
        for r in range(m):
            if matrix[r][0] == 0:
                c0 = True
                break
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0

        if r0:
            for c in range(n):
                matrix[0][c] = 0
        if c0:
            for r in range(m):
                matrix[r][0] = 0
        