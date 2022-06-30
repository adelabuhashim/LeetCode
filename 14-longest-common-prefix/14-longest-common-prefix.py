class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = min([len(i) for i in strs])
        x = len(strs)
        
        for i in range(l,0,-1):
            ind = strs[0][:i]
            if sum([ind == s[:i] for s in strs]) == x:
                return ind
        return ""
            
            