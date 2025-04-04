class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPara = 0
        closePara = 0
        for ch in s:
            if ch=='(':
                openPara+=1
            elif ch==')' and openPara>0:
                openPara-=1
            else:
                closePara+=1
        return openPara+closePara