class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l = l + 1
                r = r - 1
            return True

        if len(s) == 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                left = isValidPalindrome(s[i:j])
                right = isValidPalindrome(s[i+1:j+1])
                return left or right
            i = i + 1
            j = j - 1
        return True

        

    