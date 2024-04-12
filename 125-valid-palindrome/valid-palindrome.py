class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        res = "".join(sym for sym in lower_case if sym.isalnum())
        if res == res[::-1]:
            return True
        return False