import random as rand

class RandomizedSet:
        def __init__(self):
            self.mp = {}
            self.vals = []

        def insert(self, val: int) -> bool:
            nexists = val not in self.mp
            if nexists:
                self.mp[val] = len(self.vals)
                self.vals.append(val)
            return nexists

        def remove(self, val: int) -> bool:
            exists = val in self.mp
            if exists:
                index = self.mp[val]
                if index != len(self.vals)-1:
                    self.mp[self.vals[-1]] = index
                    self.vals[index], self.vals[-1] = self.vals[-1], self.vals[index]
                self.vals.pop()
                self.mp.pop(val)
            return exists

        def getRandom(self) -> int:
            return rand.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()