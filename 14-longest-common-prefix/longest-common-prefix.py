class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            j = 0
            while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
                j += 1
            prefix = prefix[:j]
            if prefix == "":
                break

        return prefix
        # if not strs:
        #     return ""

        # prefix = strs[0]
        # for word in strs[1:]:
        #     while not word.startswith(prefix):
        #         prefix = prefix[:-1]
        #         if not prefix:
        #             return ""

        # return prefix