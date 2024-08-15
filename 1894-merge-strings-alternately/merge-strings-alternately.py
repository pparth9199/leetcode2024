class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l=0
        r=0

        while l<len(word1) and r<len(word2):
            merged+=word1[l]
            merged+=word2[r]
            l+=1
            r+=1

        if r<len(word2):
            merged+=word2[r:]
        elif l<len(word1):
            merged+=word1[l:]

        return merged
            