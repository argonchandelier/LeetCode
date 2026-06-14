from bisect import bisect_left as bl

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = nums[:1]
        for num in nums[1:]:
            i = bl(tails, num)
            if i == len(tails):
                tails.append(num)
                continue
            tails[i] = num
        return len(tails)




        '''
        ends = [nums[0]]
        #lens = [1]
        for i, num in enumerate(nums[1:]):
            p1, p2 = 0, len(ends)-1
            while p1 <= p2:
                c = (p2+p1)//2
                #print(f"{p1 = }, {p2 = }, {c = }")
                C = ends[c]
                if C < num:
                    p1 = c+1
                    continue
                #if C >= num:
                p2 = c-1
            #ends = ends[:p1] + [num] + ends[p1:]
            if p1 == len(ends):
                ends.append(num)
            else:
                ends[p1] = num
            
            #newLen = max(lens[:p1]) + 1 if p1 > 0 else 1
            #lens = lens[:p1] + [newLen] + lens[p1:]
        #print(f"{ends = }, {lens = }")
        
        return len(ends) #max(lens)
        '''