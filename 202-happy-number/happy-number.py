class Solution:
    def isHappy(self, n: int) -> bool:
        numbers=set()
        number=0
        while True:
            for i in str(n):
                number+=int(i)**2

            if number==1:
                return True
            if number in numbers:
                return False
            numbers.add(number)
            n=number
            number=0

            