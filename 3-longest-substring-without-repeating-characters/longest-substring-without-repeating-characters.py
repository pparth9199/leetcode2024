class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(set(s)) == 1:
            return 1
        m = 0
        seen = {}
        i = 0
        for j in range(len(s)):
            if s[j] not in seen:
                seen[s[j]] = j + 1
            else:
                i = max(seen[s[j]], i)
                seen[s[j]] = j + 1
            m = max(m, (j-i)+1)
        return m

