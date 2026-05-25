class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        safe = set()
        check = []
        for r in (0, m-1):
            for c in range(n):
                if board[r][c] != 'X':
                    check.append((r,c))
        for c in (0, n-1):
            for r in range(1, m-1):
                if board[r][c] != 'X':
                    check.append((r,c))

        while check:
            r, c = check.pop()
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                r2, c2 = r+dr, c+dc
                coords = (r2, c2)
                if not (1 <= r2 < m-1) or not (1 <= c2 < n-1) or board[r2][c2] != 'O' or coords in safe:
                    continue
                safe.add(coords)
                check.append(coords)

        for r, row in enumerate(board[1:-1], start=1):
            for c in range(1, n-1):
                if row[c] != 'O' or (r,c) in safe:
                    continue
                board[r][c] = 'X'
                
        