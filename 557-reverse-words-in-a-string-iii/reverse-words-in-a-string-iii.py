class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        for i in range(len(l)):
            l[i] = l[i][::-1]
        ans = ""
        for i in range(len(l)):
            ans = ans + l[i] + " "
        ans = ans.strip()
        return ans
