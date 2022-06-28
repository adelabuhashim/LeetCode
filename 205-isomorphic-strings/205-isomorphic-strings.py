class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_2 = []
        [s_2.append(n) for n in s if n not in s_2] 
        t_2 = []
        [t_2.append(n) for n in t if n not in t_2] 
        if len(t_2) == len(s_2):
            d = {}
            for i in range(len(s_2)):
                d[s_2[i]] = t_2[i]
            print(d)
            if "".join([str(d[str(i)]) for i in s]) == t:
                return True

            
        else:
            return False