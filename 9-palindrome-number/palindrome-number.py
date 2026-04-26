class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp = x
        if x<0:
            return False
        if x<10:
            return True
        s = ""
        while x>0:
            s+=str(x%10)
            x=x//10
        return temp==int(s)