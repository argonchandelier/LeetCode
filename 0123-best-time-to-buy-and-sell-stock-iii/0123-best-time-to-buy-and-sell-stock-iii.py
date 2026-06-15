class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = -10**5, -10**5
        prof1, prof2 = 0, 0
        for i, price in enumerate(prices):
            prof2 = max(price+hold2, prof2)
            prof1 = max(price+hold1, prof1)
            hold1 = max(-price, hold1)
            if i > 1:
                hold2 = max(prof1-price, hold2)
        
        return max(prof1, prof2)
