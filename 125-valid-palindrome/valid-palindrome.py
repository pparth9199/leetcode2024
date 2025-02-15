class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        l = []
        for i in s:
            if i.isalnum():
                l.append(i)
        if l[::] == l[::-1]:
            return True
        else:
            return False

