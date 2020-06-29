class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x: int) -> None:
        if not self.data:
            self.min = x
        else:
            self.min = min(self.min, x)
        self.data.append(x)

    def pop(self) -> None:
        popped = self.data.pop()
        if popped == self.min:
            if not self.data:
                self.min = None
            else:
                self.min = min(self.data)
        return popped

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_3 = obj.top()
    print(param_3)
    print(obj.pop())
    print(obj.data)
    param_4 = obj.getMin()
    print(param_4)