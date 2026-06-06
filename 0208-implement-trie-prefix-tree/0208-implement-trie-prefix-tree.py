class Node:
    def __init__(self, c=None):
        self.c = c
        self.nexts = {}

class Trie:
    def __init__(self):
        self.root = Node()
        self.node = self.root

    def insert(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            if c in node.nexts:
                node = node.nexts[c]
                continue
            newnode = Node(c)
            node.nexts[c] = newnode
            node = newnode
        node.nexts[None] = None

    def search(self, word: str) -> bool:
        return self.startsWith(word) and None in self.node.nexts

    def startsWith(self, prefix: str) -> bool:
        self.node = self.root
        for i, c in enumerate(prefix):
            if c not in self.node.nexts:
                return False
            self.node = self.node.nexts[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)