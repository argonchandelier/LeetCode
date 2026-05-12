class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        track = set()
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i, word in enumerate(s):
            c = pattern[i]
            if c in mp:
                if mp[c] != word:
                    return False
                continue
            if word in track:
                return False
            track.add(word)
            mp[c] = word
        
        return True
