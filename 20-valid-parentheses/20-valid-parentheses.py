class Solution:
    def isValid(self, s: str) -> bool:
        p = ["()", "{}", "[]"]
        while len(s) != 0:
            if "()" not in s and "{}" not in s and "[]" not in s and len(s) != 0:
                return False
            for i in p:
                s = s.replace(i, "")

            
        return True
        