class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i + 1)
            res = max(res, s1, s2, key=len)
        return res

    def expand(self,s, l , r) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return s[l+1:r]