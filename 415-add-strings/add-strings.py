class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) -1
        p2 = len(num2) -1
        carry = 0
        res = ""
        while p1>=0 or p2>=0 or carry!=0:
            p1Val = num1[p1] if p1 >= 0 else 0
            p2Val = num2[p2] if p2 >= 0 else 0
            summ = int(p1Val) + int(p2Val) + carry
            carry = summ//10
            res+= str(summ%10)

            p1-=1
            p2-=1
        return res[::-1]