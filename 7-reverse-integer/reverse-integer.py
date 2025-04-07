class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
        else:
            sign = 1
        
        res,x = 0, abs(x)


        while x:
            mod = x%10
            x=x//10
            res = res*10 + mod

        if ((res > (2**31 - 1)) or (res < -2**31)):
            return 0
        
        return sign*res