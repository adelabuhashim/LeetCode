class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,c in enumerate(s):
            if c not in s[i+1:] and c not in s[:i]:
                return i
        return -1
        