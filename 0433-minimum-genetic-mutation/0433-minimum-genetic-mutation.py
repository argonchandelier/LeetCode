class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0
        finali = bank.index(endGene)
        base = [startGene]
        #mp = {gene: {''.join([gene[:i], '*', gene[i+1:]])}}
        seen = [False] * len(bank)
        
        res = 0
        while base:
            res += 1
            newbase = []
            for gene in base:
                for i, gene2 in enumerate(bank):
                    if seen[i]:
                        continue
                    count = 0
                    for j in range(8):
                        if gene[j] == gene2[j]:
                            count += 1
                    if count != 7:
                        continue
                    if i == finali:
                        return res
                    seen[i] = True
                    newbase.append(gene2)
            base = newbase
        return -1
                        