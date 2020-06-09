class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if not s:
            return True
        if len(s) > len(t):
            return False
        
        ps = 0
        pt = 0
        res = ""
        
        while ps < len(s) and pt < len(t):
            
            if s[ps] == t[pt]:
                res += s[ps]
                ps += 1
                pt += 1
                
            else:
                pt += 1
            
        return res == s