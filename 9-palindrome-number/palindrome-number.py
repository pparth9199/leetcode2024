class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]

        # Without str conversion
        if x<0:
            return False
        if x==0:
            return True
        def reverse(num,n):
            if n==0:
                return num
            current = num%10
            remain = num//10
            return (current * 10**(n)) + reverse(remain,n-1)
        return x==reverse(x,len(str(x))-1)