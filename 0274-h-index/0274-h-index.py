class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):
            if i >= c:
                return max(c, i-1)
        return len(citations)
