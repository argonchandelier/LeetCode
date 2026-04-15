class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        n = len(words)
        limit = n // 2
        p1, p2 = startIndex, startIndex
        for step in range(1, limit+1):
            p1, p2 = p1-1, p2+1
            if words[p1] == target or words[p2 % n] == target:
                return step
        
        return -1
