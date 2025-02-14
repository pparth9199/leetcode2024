class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0 or len(s)==1:
            return True
        s = s.replace(" ", "")
        translator = str.maketrans('', '', string.punctuation)
        s = s.translate(translator)
        s = s.lower()
        p2 = len(s) - 1
        for p1 in range(0,len(s)//2):
            if s[p1] != s[p2]:
                return False
            p2 = p2 - 1
        return True
