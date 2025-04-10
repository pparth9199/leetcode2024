class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n=digits[-1]+1
        num = n%10
        carry=n//10
        digits[-1]=num
        if carry==0:
            return digits
        else:
            for i in range(len(digits)-2,-1,-1):
                n=digits[i]+carry
                num = n%10
                carry=n//10
                digits[i]=num
                if carry==0:
                    return digits

            if carry!=0:
                digits.insert(0,carry)

        return digits

        
            