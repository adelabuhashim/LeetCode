class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = dict(Counter(ransomNote))
        magazine = dict(Counter(magazine))
        for k,v  in ransomNote.items():
            if k not in magazine.keys() or v > magazine[k]:
                return False
        return True