class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        if not s:
            return 0
        l = 0
        n = 0
        s = list(s)
        ss = {}
        for r in range(len(s)):
            if s[r] in ss:
                l = max(l, ss[s[r]])
            c = r - l + 1
            n = max(n, c)
            ss[s[r]] = r + 1
        return n
            