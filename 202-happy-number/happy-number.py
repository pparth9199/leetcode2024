class Solution:
    def isHappy(self, n: int) -> bool:
        numbers={}
        number=0
        while True:
            for i in str(n):
                number+=int(i)**2

            if number==1:
                return True
            if number in numbers:
                return False
            numbers[number]=0
            n=number
            number=0

            