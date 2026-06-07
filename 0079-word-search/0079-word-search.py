class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.seen = set()
        m, n, l = len(board), len(board[0]), len(word)
        def bt(r, c, i):
            if i == l:
                return True
            for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
                r2, c2 = r+dr, c+dc
                if not (0 <= r2 < m and 0 <= c2 < n) or board[r2][c2] != word[i]:
                    continue 
                coords = (r2, c2)
                if coords in self.seen:
                    continue
                self.seen.add(coords)
                res = bt(r2, c2, i+1)
                if res:
                    return True
                self.seen.remove(coords)
            return False
            
        for r in range(m):
            for c in range(n):
                char = board[r][c]
                if char != word[0]:
                    continue
                self.seen.add((r,c))
                if bt(r, c, 1):
                    return True
                self.seen = set()
        return False