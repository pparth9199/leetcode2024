class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = list(s)
        l2 = list(t)
        for i in l1:
            if i in l2:
                l2.remove(i)
            else:
                return False
        return True
        