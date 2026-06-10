import heapq
class MedianFinder:
    def __init__(self):
        self.mid = None
        self.left = [10**6]
        self.right = [10**6]

    def addNum(self, num: int) -> None:
        if self.mid is None:
            l, r = -self.left[0], self.right[0]
            if num < l:
                self.mid = l
                heapq.heappushpop(self.left, -num)
            elif num > r:
                self.mid = r
                heapq.heappushpop(self.right, num)
            else:
                self.mid = num
            return

        if num < self.mid:
            heapq.heappush(self.left, -num)
            heapq.heappush(self.right, self.mid)
        else:
            heapq.heappush(self.right, num)
            heapq.heappush(self.left, -self.mid)
        self.mid = None

    def findMedian(self) -> float:
        return self.mid if self.mid is not None else (self.right[0] - self.left[0]) / 2.

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()