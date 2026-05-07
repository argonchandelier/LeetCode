conv = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
sub = {4, 9}


class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        while num > 0:
            s = str(num)
            l = len(s)
            n = int(s[0])
            add = 10**(l-1)
            if n in sub:
                num += add
                res.append(conv[add])
                continue
            if n >= 5:
                add *= 5
            num -= add
            res.append(conv[add])

        return ''.join(res)        