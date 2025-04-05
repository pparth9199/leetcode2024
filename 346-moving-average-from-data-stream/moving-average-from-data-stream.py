class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.storage = deque()
        self.current_sum = 0

    def next(self, val: int) -> float:
        self.storage.append(val)
        self.current_sum += val
        current_size = len(self.storage)
        if current_size > self.size:
            removed_val = self.storage.popleft()
            self.current_sum -= removed_val
            return self.current_sum/self.size
        else:
            return self.current_sum/current_size

        
        if current_size < self.size:
            return sum(self.storage)/current_size
        else:
            return sum(self.storage[-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)