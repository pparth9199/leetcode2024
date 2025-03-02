class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        if len(s) == 0 or len(s) == 1:
            return True
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i
        return new_s[::] == new_s[::-1]