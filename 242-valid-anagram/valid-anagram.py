class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = defaultdict(int)
        for i in range(len(s)):
            d1[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in d1:
                return False
            d1[t[i]] -= 1
        for i in d1.values():
            if i:
                return False
        return True