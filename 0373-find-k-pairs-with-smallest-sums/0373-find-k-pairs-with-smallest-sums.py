import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        res = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        n1used = 0
        for c in range(k):
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            i2, j2 = i + 1, j + 1
            if j2 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j2], i, j2))
            if j == 0 and i2 < m:
                heapq.heappush(heap, (nums1[i2] + nums2[j], i2, j))
        
        return res
