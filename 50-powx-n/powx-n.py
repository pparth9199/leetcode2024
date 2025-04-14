class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary(x , n) -> float:
            if n == 0:
                return 1
            
            if n < 0:
                return 1.0 / binary(x, -1 * n)
            
            if n % 2 == 0:
                return binary(x * x, n // 2)
            else:
                return x * binary(x * x, (n-1)//2)
            
        return binary(x, n)