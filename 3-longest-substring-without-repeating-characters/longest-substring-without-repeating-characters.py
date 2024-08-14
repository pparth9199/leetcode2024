class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        l,r,maxLength=0,0,0
        while(r<len(s)):
            if s[r] in hashmap and hashmap[s[r]]>=l:
                l=hashmap[s[r]]+1
            length = r-l+1
            maxLength=max(maxLength,length)
            hashmap[s[r]]=r
            r+=1
        return maxLength