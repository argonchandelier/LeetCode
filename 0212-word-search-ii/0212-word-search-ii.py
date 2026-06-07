class Node:
    def __init__(self, i=None, ch=None):
        self.i = i
        self.ch = ch
        self.adjs = defaultdict(set)

class TrieNode:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        nodes = [[None]*n for _ in range(m)]
        self.seen = [False]*m*n
        chrs = set()
        index = 0

        trieroot = {}
        def dfs0(node, i):
            if i == len(self.word):
                node[''] = {None: self.word}
                return
            ch = self.word[i]
            if ch in node:
                node2 = node[ch]
                dfs0(node2, i+1)
                return
            newnode = {}
            node[ch] = newnode
            node = newnode
            dfs0(node, i+1)
        for word in words:
            self.word = word
            dfs0(trieroot, 0)


        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                chrs.add(ch)
                node = Node(index, ch)
                index += 1
                nodes[r][c] = node
                if r > 0:
                    node2 = nodes[r-1][c]
                    node2.adjs[ch].add(node)
                    node.adjs[node2.ch].add(node2)
                if c > 0:
                    node2 = nodes[r][c-1]
                    node2.adjs[ch].add(node)
                    node.adjs[node2.ch].add(node2)
        
        root = Node()
        for r in range(m):
            for c in range(n):
                node = nodes[r][c]
                root.adjs[node.ch].add(node)
        
        self.res = set()
        self.wordsplit = []
        def dfs1(trienode, node):
            for ch in trienode:
                if ch == '':
                    self.res.add(trienode[''][None])
                    continue
                if ch in node.adjs:
                    for node2 in node.adjs[ch]:
                        if self.seen[node2.i]:
                            continue
                        self.seen[node2.i] = True
                        dfs1(trienode[ch], node2)
                        self.seen[node2.i] = False
        
        dfs1(trieroot, root)
        return list(self.res)

        '''
        res = []
        def dfs(node, i):
            if i == len(self.word):
                return True
            ch = self.word[i]
            if ch not in node.adjs:
                return False
            for node2 in node.adjs[ch]:
                if self.seen[node2.i]:
                    continue
                self.seen[node2.i] = True
                r = dfs(node2, i+1)
                self.seen[node2.i] = False
                if r:
                    return True
            return False
        for word in words:
            for c in word:
                if c not in chrs:
                    break
            else:
                self.word = word
                if dfs(root, 0):
                    res.append(word)
        
        return res
        '''
        
