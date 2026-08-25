class FreqStack:
    def __init__(self):
        self.m = {}
        self.stacks = {}
        self.i = 0

    # move val from one freq up to next
    def push(self, val: int) -> None:
        if val not in self.m:
            self.m[val] = 1
        else:
            self.m[val] += 1 

        valCount = self.m[val]

        if valCount > self.i:
            self.i += 1
            self.stacks[valCount] = []

        self.stacks[valCount].append(val)

    # at index
    def pop(self) -> int:
        res = self.stacks[self.i].pop()
        self.m[res] -= 1
        if not self.stacks[self.i]:
            self.i -= 1

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()