from functools import lru_cache

class Solution:
    @lru_cache
    def rc(self, ns):
        r = self.nm1 - (ns // self.n)
        c = ns % self.n if (self.n+r)&1 == 1 else self.nm1 - (ns % self.n)
        return r, c

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = n = len(board)
        f = n**2
        self.nm1, fm1 = n-1, f-1
        seen = [False]*f
        seen[0] = True

        spaces = [0]
        rolls = 0
        while spaces:
            rolls += 1
            nspaces = []
            for space in spaces:
                for add in range(1,7):
                    nspace = space + add
                    if nspace >= fm1:
                        if nspace == fm1:
                            return rolls
                        break
                    
                    r, c = self.rc(nspace)
                    val = board[r][c]
                    if val == -1:
                        if seen[nspace]:
                            continue
                        seen[nspace] = True
                        nspaces.append(nspace)
                        continue

                    nspace2 = val-1
                    if nspace2 == fm1:
                        return rolls
                    if seen[nspace2]:
                        continue
                    seen[nspace2] = True
                    nspaces.append(nspace2)
            spaces = nspaces

        return -1