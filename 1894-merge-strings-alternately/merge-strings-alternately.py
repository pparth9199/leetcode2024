class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        p1 = 0
        p2 = 0
        new = ""
        while p1 < n1 and p2 < n2:
            new += word1[p1]
            p1 += 1
            new += word2[p2]
            p2 += 1
        if p1 < n1:
            new += word1[p1:n1]
        if p2 < n2:
            new += word2[p2:n2]
        return new