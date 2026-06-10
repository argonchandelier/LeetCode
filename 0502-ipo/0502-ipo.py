import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        nprofcaps = [(-p, c) for p, c in zip(profits, capital)]
        nprofcaps.sort(key=lambda x: x[1])
        self.entered = 0
        self.heap = []

        def update():
            while self.entered < n and nprofcaps[self.entered][1] <= w:
                heapq.heappush(self.heap, nprofcaps[self.entered][0])
                self.entered += 1
        
        update()
        while self.heap and k > 0:
            w += -heapq.heappop(self.heap)
            k -= 1
            update()
        
        return w

        