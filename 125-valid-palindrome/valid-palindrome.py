class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.translate(str.maketrans('', '', string.punctuation))
        s=s.replace(" ","")
        s=s.lower()
        left=0
        right=len(s)-1

        while left<right:
            if s[left].lower()!=s[right].lower():
                return False

            left+=1
            right-=1
        return True
            