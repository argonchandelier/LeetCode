dx = (-1, 0, 1)
live = {2, 3}

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                count = 0
                val = board[r][c]
                for dr in dx:
                    for dc in dx:
                        if dr == dc == 0:
                            continue
                        r2, c2 = r+dr, c+dc
                        if 0 <= r2 < m and 0 <= c2 < n:
                            count += board[r2][c2] % 2
                if (val == 1 and count in live) or (val == 0 and count == 3):
                    board[r][c] += 2
        
        for r in range(m):
            for c in range(n):
                board[r][c] = board[r][c] // 2

                
        