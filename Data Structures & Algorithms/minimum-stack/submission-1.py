class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None or val < self.min:
            self.min = val

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        else:
            self.min = min(self.stack)

        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
