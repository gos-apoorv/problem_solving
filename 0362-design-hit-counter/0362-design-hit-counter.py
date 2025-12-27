class HitCounter:

    def __init__(self):
        self.hit_array = []
        
    def hit(self, timestamp: int) -> None:
        self.hit_array.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if len(self.hit_array) == 0:
            return 0
        
        while self.hit_array[0] <= timestamp-300:
            self.hit_array.pop(0)
            if not self.hit_array:
                break
        return len(self.hit_array)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)