class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.storage = []

    def next(self, val: int) -> float:
        self.storage.append(val)
        
        return sum(self.storage[-self.size:]) / min(self.size, len(self.storage))

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)