class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scount=Counter(s)
        tcount=Counter(t)

        return list((tcount-scount).keys())[0]
        # extra=""
        # l,r=0,0
        # while l<len(s) and r<len(t):
        #     if s[l]!=t[r]:
        #         return t[r]
        #     l+=1
        #     r+=1
        
        # return t[-1]