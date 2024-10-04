class BrowserHistory:

    def __init__(self, homepage: str):
        self.stk = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:

        val_at_index = self.stk[self.index]

        while(self.stk[-1]!=val_at_index):
            self.stk.pop()
        
        self.stk.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        while(self.index>0 and steps>0 ):
            self.index = self.index -1
            steps = steps -1
        
        ind = self.index
        return self.stk[ind]

    def forward(self, steps: int) -> str:
        l = len(self.stk)

        while(self.index<l-1 and steps > 0):
            self.index = self.index +1
            steps = steps -1
        ind = self.index
        return self.stk[ind]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)