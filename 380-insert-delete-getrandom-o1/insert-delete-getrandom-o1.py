import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.length = 0


    def insert(self, val: int) -> bool:
        if val in self.dict:
            # print("insert", self.dict)
            return False
        self.dict[val] = 0
        self.length += 1
        # print("insert", self.dict)
        return True


    def remove(self, val: int) -> bool:
        if val in self.dict:
            del self.dict[val]
            self.length -= 1
            # print("remove", self.dict)
            return True
        # print("remove", self.dict)
        return False


    def getRandom(self) -> int:
        elements = list(self.dict.keys())
        random_element = random.choice(elements)
        # print("random", self.dict)
        return random_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()