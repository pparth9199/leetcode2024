class Solution:
    def reverse(self, x: int) -> int:
        if x>=(2**31)-1 or x<=-2**31:
            return 0
        def helper(num,n):
            if n==0:
                return num
            current = num%10
            remain = num//10
            return (current * 10**(n)) + helper(remain,n-1)
        reversedNum = helper(abs(x),len(str(abs(x)))-1) * (-1 if x<0 else 1)
        if reversedNum>=(2**31)-1 or reversedNum<=-2**31:
            return 0
        return reversedNum