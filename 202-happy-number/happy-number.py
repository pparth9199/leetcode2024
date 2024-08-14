class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            return sum(int(i) ** 2 for i in str(number))
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)          # Moves one step
            fast = get_next(get_next(fast)) # Moves two steps
        
        return fast == 1
