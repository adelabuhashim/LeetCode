class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = min([len(i) for i in strs])
        x = len(strs)
        
        for i in range(l,0,-1):
            if sum([strs[0][:i] == s[:i] for s in strs]) == x:
                print(strs[0])
                return strs[0][:i]
        return ""
            
            