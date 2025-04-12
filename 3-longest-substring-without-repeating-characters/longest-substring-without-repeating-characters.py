class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars=set()
        res=0
        right=0
        while right<len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            res=max(res,right-left+1)
            right+=1
        return res
            
        # chars = set()
        # result = 0

        # for right in range(len(s)):
        #     while s[right] in chars:
        #         chars.remove(s[left])
        #         left += 1
        #     chars.add(s[right])
        #     result = max(result, right - left + 1)

        # return result