class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers)-1
        while True:
            goal = target - numbers[p1]
            while numbers[p2] > goal:
                p2 -= 1
            if numbers[p2] == goal:
                return [p1+1, p2+1]
            p1 += 1