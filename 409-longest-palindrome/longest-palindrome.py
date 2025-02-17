class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(set(s)) == 1:
            return len(s)
        d = {}
        l = 0
        odd = 1
        for i in set(s):
            d[i] = s.count(i)
        for i in d:
            if d[i] % 2 == 0 :
                l = l + d[i]
            elif d[i] == 1 and odd == 1:
                l = l + d[i]
                odd = odd + 1
            elif d[i] % 2 != 0 and d[i] > 2:
                if odd == 1:
                    l = l + d[i]
                    odd = odd + 1
                else:
                    l = l + d[i] - 1
        return l