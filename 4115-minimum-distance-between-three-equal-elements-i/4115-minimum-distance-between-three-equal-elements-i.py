class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freqs = {}
        dist = float('inf')
        for i, n in enumerate(nums):
            if n not in freqs:
                freqs[n] = [i]
                continue
            if len(freqs[n]) < 3:
                freqs[n].append(i)
                if len(freqs[n]) < 3:
                    continue
            else:
                freqs[n][0], freqs[n][1], freqs[n][2] = freqs[n][1], freqs[n][2], i
            dist = min(dist, 2*(freqs[n][2]-freqs[n][0]))

        return dist if dist < float('inf') else -1