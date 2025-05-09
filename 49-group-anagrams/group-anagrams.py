class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            ordList = [0]*26

            for char in word:
                ordList[ord(char) - ord('a')] +=1

            grouped[tuple(ordList)].append(word)


        return list(grouped.values())

         