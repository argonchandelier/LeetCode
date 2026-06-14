class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0]
        for i, row in enumerate(triangle[1:], start=1):
            ndp = [row[0] + dp[0]]
            for j in range(1, len(dp)):
                ndp.append(row[j] + min(dp[j-1], dp[j]))
            ndp.append(dp[-1] + row[-1])
            dp = ndp
        return min(dp)