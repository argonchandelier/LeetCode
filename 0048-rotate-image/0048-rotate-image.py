class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
        