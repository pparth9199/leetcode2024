class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counting = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            counting[s[right]]+=1
            while len(counting) >2:
                counting[s[left]] -= 1
                if counting[s[left]] == 0:
                    del counting[s[left]] 
                left += 1
            
            res = max(res,right-left+1)

        return res
            