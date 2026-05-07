import random as rand

class RandomizedSet:
        def __init__(self):
            self.vals = set()

        def insert(self, val: int) -> bool:
            nexists = val not in self.vals
            if nexists:
                self.vals.add(val)
            return nexists

        def remove(self, val: int) -> bool:
            exists = val in self.vals
            if exists:
                self.vals.remove(val)
            return exists

        def getRandom(self) -> int:
            return rand.choice(list(self.vals))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()