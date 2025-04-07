class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        words = sentence.split(" ")
        res = []
        for i in range(len(words)):
            adder = "ma"+"a" * (i + 1)
            if words[i][0] in vowels:
                res.append(words[i]+adder)
            else:
                word = words[i][1:]+words[i][0]+adder
                res.append(word)

        return " ".join(res)