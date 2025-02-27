class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # visited = defaultdict(int)
        # l = 0
        # r = 0
        # ans = 0
        # while l < len(s) and r < len(s):
        #     if s[r] not in visited or visited[s[r]] < 2:
        #         ans = max(ans, r - l + 1)
        #         visited[s[r]] += 1
        #         r = r + 1
        #     else:
        #         l = l + 1
        #         visited[s[l]] -= 1
        # return ans
        if len(s) > 2 and len(set(s)) == 1:
            return 2

        d = defaultdict(int)
        l = 0
        r = 0
        res = 0

        while l < len(s) and r < len(s):
            if s[r] not in d or d[s[r]] < 2:
                d[s[r]] +=1
                res = max(res, r - l + 1)
                r+=1
            else:
                d[s[l]]-=1
                l+=1
        return res