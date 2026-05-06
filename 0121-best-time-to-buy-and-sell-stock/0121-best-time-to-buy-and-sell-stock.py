class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
                continue
            diff = prices[i]-mn
            if diff > mp:
                mp = diff
        
        return mp