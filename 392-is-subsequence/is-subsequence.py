class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r=0,0
        if not s:
            return True
        if len(s)>len(t):
            return False
        while r<len(t) and l<len(s):
            if s[l]==t[r]:
                l+=1
            r+=1
        return l==len(s)
        
