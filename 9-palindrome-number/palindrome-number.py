class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        def helper(num,n):
            if n==0:
                return num
            current = num%10
            remain = num//10
            return (current * 10**(n)) + helper(remain,n-1)
        return x==helper(x,len(str(x))-1)