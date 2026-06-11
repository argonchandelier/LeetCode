class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(-1, -len(digits)-1, -1):
            carry, digits[i] = divmod(digits[i]+carry, 10)
            if carry < 1:
                break
        else:
            res = [0]*(len(digits)+1)
            res[0] = 1
            return res
        return digits