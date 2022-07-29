class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        words = [word for word in words if len(word) == len(pattern) and len(set(word)) == len(set(pattern))]
        pattern_ch = []
        [pattern_ch.append(i) for i in pattern if i not in pattern_ch]
        result = []
        for word in words:
            ch = []
            [ch.append(i) for i in word if i not in ch]
            word_ = ""
            for c in word:
                word_ += pattern_ch[ch.index(c)]
            if word_ == pattern:
                result.append(word)
        return result