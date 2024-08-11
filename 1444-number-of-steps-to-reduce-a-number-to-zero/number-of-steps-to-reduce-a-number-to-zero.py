class Solution:
    def numberOfSteps(self, num: int) -> int:
        def reduceCounter(n,count):
            if n==0:
                return count
            return reduceCounter(n/2,count+1) if n%2==0 else reduceCounter(n-1,count+1)
        return reduceCounter(num,0)