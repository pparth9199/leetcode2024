class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0 or len(s) == 1:
            return True
        l = []
        for i in s:
            if i.isalnum():
                l.append(i)
        news = "".join(l)
        news = news.lower()
        print(news)
        if news[::] == news[::-1]:
            return True
        else:
            return False

