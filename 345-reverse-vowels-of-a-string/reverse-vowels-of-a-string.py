class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        arr=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        while l<=r:

            if s[l] in arr and s[r] in arr:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] in arr and s[r] not in arr:
                r-=1
            elif s[l] not in arr and s[r] in arr:
                l+=1
            else:
                l+=1
                r-=1

        return "".join(s)
