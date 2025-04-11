class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry=0
        i=len(num)-1
        while k > 0 or carry > 0 or i>=0 :
            current = k % 10
            k = k // 10
            n = num[i] if i >= 0 else 0
            current_sum = current + carry + n
            carry = current_sum // 10
            digit = current_sum % 10

            if i >= 0:
                num[i] = digit
            else:
                num.insert(0, digit)
            i-=1
        return num
        
        if k!=0:
            num.insert(0,k)
        if carry>0:
            num.insert(0,carry)
        return num