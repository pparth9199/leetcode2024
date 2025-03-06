class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_count=Counter(s)
        t_count = Counter(t)
        return s_count == t_count