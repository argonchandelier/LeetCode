class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profits = [0]*(k+1)
        holds = [-1000]*k
        for i, price in enumerate(prices):
            for j in range(1, k+1):
                nprof = holds[j-1] + price
                if nprof > profits[j]:
                    profits[j] = nprof
                if profits[j] == 0:
                    break
            
            for j in range(min(k, (i//2)+1)):
                nhold = profits[j] - price
                if nhold > holds[j]:
                    holds[j] = nhold

        return max(profits)