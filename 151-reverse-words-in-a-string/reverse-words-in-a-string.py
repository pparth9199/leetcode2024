class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        filtered_list = list(filter(None, ls))
        filtered_list = filtered_list[::-1]
        return " ".join(filtered_list)