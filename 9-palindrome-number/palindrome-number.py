class Solution:
    def isPalindrome(self, x: int) -> bool: #121
        temp = x
        if x<0:
            return False
        if x<10:
            return True
        reverse =0 
        while x>0:
            reverse = (reverse*10)+(x%10) #reverse = 12
            x=x//10 #x=12
        return temp==reverse