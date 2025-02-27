class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        visited = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        while l < len(s) and r < len(s):
            if s[r] not in visited or visited[s[r]] < 2:
                ans = max(ans, r - l + 1)
                visited[s[r]] += 1
                r = r + 1
            else:
                visited[s[l]] -= 1
                l = l + 1
        return ans