class TwoSum:

    def __init__(self):
        self.arr=[]
        self.checker={}

    def add(self, number: int) -> None:
        for i in self.arr:
            self.checker[i+number]=[i,number]
        self.arr.append(number)


    def find(self, value: int) -> bool:
        return value in self.checker
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)