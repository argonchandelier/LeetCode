class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
                continue
            node[c] = {}
            node = node[c]
        node[''] = {}

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for c in word:
            if not nodes:
                return False
            newnodes = []
            for node in nodes:
                if c == '.':
                    for key in node:
                        newnodes.append(node[key])
                    continue
                if c in node:
                    newnodes.append(node[c])
            nodes = newnodes
        for node in nodes:
            if '' in node:
                return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)