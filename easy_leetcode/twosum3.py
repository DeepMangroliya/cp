class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
            self.nums.append(number)

    def find(self, value: int) -> bool:
        seen = set()
        for element in self.nums:
            complement = value - element
            if complement in seen:
                return True
            seen.add(element)
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)