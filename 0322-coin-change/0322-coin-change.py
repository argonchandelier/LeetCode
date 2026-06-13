from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        amts = [False]*(amount+1)
        amts[0] = True
        curs = [0]
        res = 0
        while curs:
            newcurs = []
            res += 1
            for cur in curs:
                for coin in coins:
                    ncur = cur+coin
                    if ncur > amount or amts[ncur]:
                        continue
                    if ncur == amount:
                        return res
                    amts[ncur] = True
                    newcurs.append(ncur)
            curs = newcurs
        return -1