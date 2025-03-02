class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l , r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l = l + 1
                r = r - 1
            return True
        
        if len(s) == 1:
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left = isPalindrome(s, l, r-1)
                right = isPalindrome(s, l+1, r)
                return left or right
            l = l + 1
            r = r - 1        
        return True