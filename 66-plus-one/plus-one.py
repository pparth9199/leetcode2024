class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cachedAdder, digit = 1,len(digits)-1
        
        while cachedAdder:
            print(digits[digit])
            if digit>=0:
                if digits[digit] == 9:
                    digits[digit]=0
                else:
                    digits[digit]+=1
                    cachedAdder=0
            else:
                digits.insert(0,1)
                cachedAdder=0
            digit-=1
        
        return digits
                