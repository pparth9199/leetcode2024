class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left,right=0,0
        list_s=[]
        max_len = float('-inf')

        while right<len(s):
            list_s.append(s[right])
            while len(set(list_s))>k:
                del list_s[0]
                left+=1
            
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len