from typing import List
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Step 1: Split nums into two halves
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]

        # Step 2: Calculate all subset sums for each half
        left_sums = self.calculate_subset_sums(left)
        right_sums = self.calculate_subset_sums(right)

        ###
        min_diff = float('inf')
        total_sum = sum(nums)

        for k in range(n+1):
            ls = left_sums[k]
            rs = right_sums[n-k]
            min_diff = min(min_diff, self.find_min_diff(ls, rs, total_sum))
        
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
        n = len(arr)
        sums = [set() for _ in range(n + 1)]
        sums[0] = {0}
        for x in arr:
            for k in range(n, 0, -1):
                for s in sums[k-1]:
                    sums[k].add(s + x)
        
        return [sorted(list(s)) for s in sums]

        # Your code for calculating subset sums ends here

    def find_min_diff(self, left_sums: List[int], right_sums: List[int], total_sum: int) -> int:
        """
        Find the minimum possible absolute difference between the sums of two partitions.

        Args:
            left_sums (List[int]): List of subset sums from the first half of nums.
            right_sums (List[int]): Sorted list of subset sums from the second half of nums.
            total_sum (int): The sum of all elements in nums.

        Returns:
            int: The minimum possible absolute difference.
        """
        min_diff = float('inf')

        # Iterate over all subset sums from the left half
        for s in left_sums:
            # Target sum to achieve minimal difference
            target = total_sum // 2 - s

            # Binary search to find the closest sum in right_sums to 'target'
            idx = bisect.bisect_left(right_sums, target)

            # Check two closest values to minimize the difference
            if idx < len(right_sums):
                min_diff = min(min_diff, abs(total_sum - 2 * (s + right_sums[idx])))

            if idx > 0:
                min_diff = min(min_diff, abs(total_sum - 2 * (s + right_sums[idx - 1])))

        return min_diff


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [3, 9, 7, 3],
        [-36, 36],
        [2, -1, 0, 4, -2, -9]
    ]

    # Creating an instance of the Solution class
    solution = Solution()

    # Running the test cases
    for i, nums in enumerate(test_cases, 1):
        print(f"Test case {i}: nums = {nums}")
        result = solution.minimumDifference(nums)
        print(f"Minimum possible absolute difference: {result}\n")