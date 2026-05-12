class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        track = [set() for _ in range(27)]
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                for i in (r, 9+c, 18+r//3+3*(c//3)):
                    if val == '.':
                        continue
                    if val in track[i]:
                        return False
                    track[i].add(val)
        
        return True