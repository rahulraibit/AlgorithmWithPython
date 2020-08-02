class MinStack:

    def __init__(self):
        self.min = [];
        self.stack = [];
        

    def push(self, x: int) -> None:
        if len(self.min) == 0:
            self.min.append(x);
        elif x <= self.min[len(self.min) - 1]:
            self.min.append(x);
        self.stack.append(x);
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[len(self.stack)-1] == self.min[len(self.min) - 1]:
                self.min.pop();
            self.stack.pop();
        

    def top(self) -> int:
         if len(self.stack) > 0:
            return self.stack[len(self.stack)-1];
         else:
            return None;
        

    def getMin(self) -> int:
        if len(self.min) > 0:
            return self.min[len(self.min)-1];
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()