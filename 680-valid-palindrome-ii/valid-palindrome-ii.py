class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            return s[:] == s[::-1]
        
        if len(s) == 1:
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                new_s = s[l+1:r+1]
                new_s1 = s[l:r]
                return isPalindrome(new_s) or isPalindrome(new_s1)
            l = l + 1
            r = r - 1 
        return True       