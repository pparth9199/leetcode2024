class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.storage = []

    def next(self, val: int) -> float:
        self.storage.append(val)
        current_size = len(self.storage)
        if current_size < self.size:
            return sum(self.storage)/current_size
        else:
            return sum(self.storage[-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)