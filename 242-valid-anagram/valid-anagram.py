class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=Counter(s)
        for x in t:
            count[x]-=1
        
        for c in count.values():
            if c!=0:
                return False
        return True
            