class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = len(gas)-1
        G = 0
        mn = 0
        for i in range(len(gas)):
            G -= cost[i-1]
            if G < mn:
                mn = G
                res = i
            G += gas[i]
        return res if G >= 0 else -1