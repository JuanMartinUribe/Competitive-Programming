class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.last = -1
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.last = x
    def pop(self) -> int:
        for _ in range(len(self.q1)-1):
            last = self.q1.popleft()
            self.q1.append(last)
            self.last = last
        return self.q1.popleft() 
    def top(self) -> int:
        return self.last
    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()