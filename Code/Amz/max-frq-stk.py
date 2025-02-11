class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.maxCount = 0
        self.stks = defaultdict(list)

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.maxCount = max(self.maxCount, self.count[val])
        
        self.stks[self.count[val]].append(val)

    def pop(self) -> int:
        # print('cnt',self.count)
        # print('stk', self.stks)
        # print('max',self.maxCount)
        popVal = self.stks[self.maxCount].pop()
        self.count[popVal] -= 1
        
        if(not self.stks[self.maxCount]):
            self.maxCount -= 1
        
        return popVal
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()