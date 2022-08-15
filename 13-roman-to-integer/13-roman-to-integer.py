class Solution:
    def romanToInt(self, s: str) -> int:
        essential = {"I": 1, "V":5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000,
        }
        specials = {"IV": 4, "IX":9, "XL":40,"XC":90 ,"CD":400, "CM":900} 
        result = 0
        for k,v in  specials.items():
            if k in s:
                s = s.replace(k, "")
                result += v
        print(result)
        for c in s:
                result += essential[c]
        return result