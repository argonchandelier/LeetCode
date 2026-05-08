class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        start = 0
        nc, nw = len(words[0]), 1
        lines = []
        for i, word in enumerate(words[1:], start=1):
            l = len(word)
            nca = l + 1
            if maxWidth >= nc+nca:
                nw += 1
                nc += nca
                continue

            # overflowing; add line
            if nw > 1:
                nspaces, extra = divmod(maxWidth-nc+nw-1, nw-1)
            else:
                nspaces, extra = maxWidth-nc, 0
            txt = [words[start]]
            short = ''.join([" "]*nspaces)
            lng = short+" " if extra > 0 else short
            for j in range(1, nw):
                k = start+j
                if extra > 0:
                    txt.append(lng)
                    extra -= 1
                else:
                    txt.append(short)
                txt.append(words[k])
            if nw == 1:
                txt.extend(short)
            lines.append(''.join(txt))
            start = i
            nc, nw = l, 1

        txt = [words[start]]
        txtl = len(words[start])
        for j in range(start+1, len(words)):
            txt.append(" ")
            txt.append(words[j])
            txtl += 1+len(words[j])
        txt.extend([" "]*(maxWidth - txtl))
        lines.append(''.join(txt))

        return lines
            

