class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for i in magazine:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        r = {}
        for j in ransomNote:
            if j in r:
                r[j] += 1
            else:
                r[j] = 1
        for i in ransomNote:
            if i not in m or (m[i] < r[i]):
                return False
        return True