class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = -10**5, -10**5
        prof1, prof2 = 0, 0
        for i, price in enumerate(prices):
            np2, np1, nh1, nh2 = price+hold2, price+hold1, -price, prof1-price
            if np2 > prof2:
                prof2 = price+hold2
            if np1 > prof1:
                prof1 = price+hold1
            if nh1 > hold1:
                hold1 = -price
            if nh2 > hold2 and i > 1:
                hold2 = prof1-price
        
        return max(prof1, prof2)
