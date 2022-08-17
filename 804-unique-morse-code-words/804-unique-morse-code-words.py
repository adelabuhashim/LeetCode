import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        chars = [i for i in string.ascii_lowercase]
        converter = {chars[i]: code[i] for i in range(len(chars))}
        res = []
        for w in words:
            word = ""
            for c in w:
                word +=  converter[c]
            if word not in res:
                res.append(word)
        return len(res)
            
