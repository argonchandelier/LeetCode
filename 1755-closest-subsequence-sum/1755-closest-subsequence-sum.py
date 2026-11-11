from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal) -> int:
        # Step 1: Split nums into two halves
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]

        # Step 2: Calculate all subset sums for each half
        left_sums = self.calculate_subset_sums(left)
        right_sums = self.calculate_subset_sums(right)

        # Step 3: Sort right_sums for binary search efficiency
        right_sums.sort()

        # Step 4: Find minimum absolute difference
        min_diff = self.find_min_diff(left_sums, right_sums, goal)
        return min_diff

    def calculate_subset_sums(self, arr: List[int]) -> List[int]:
        """
        Calculate all possible subset sums for a given list.

        Args:
            arr (List[int]): The list of integers for which subset sums are calculated.

        Returns:
            List[int]: A list of all subset sums of the input list.
        """
        # Your code for calculating subset sums starts here
        sums = {0}
        for x in arr:
            for s in sums.copy():
                sums.add(s+x)
        
        return list(sums)

        # Your code for calculating subset sums ends here

    def find_min_diff(self, left_sums: List[int], right_sums: List[int], goal: int) -> int:
        min_diff = float('inf')

        for s in left_sums:
            target = goal - s
            idx = bisect.bisect_left(right_sums, target)

            if idx < len(right_sums):
                min_diff = min(min_diff, abs(target - right_sums[idx]))

            if idx > 0:
                min_diff = min(min_diff, abs(target - right_sums[idx - 1]))

        return min_diff