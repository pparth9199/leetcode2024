class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=len(s)-1
        word=""
        while r>=0:
            if s[r]==' ':
                if len(word)<1:
                    r-=1
                    continue
                else:
                    break
            word+=s[r]
            r-=1
        return len(word)
                
