
class MinStack:

    def __init__(self): # O(1)
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if self.min is None:
            self.min = val
        elif val <= self.min:
            self.min = val



    def pop(self) -> None: # O(1)
        if self.top() == self.getMin():
            self.min = self.stack[-1][1]
        self.stack.pop(-1)


    def top(self) -> int: # O(1)
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
