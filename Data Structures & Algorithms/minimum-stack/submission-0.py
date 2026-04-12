class MinStack:

    def __init__(self):
        self.stackElem = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stackElem.append(val)
        
        if self.stackMin:
            minVal = min(self.stackMin[-1], val)
        else:
            minVal = val
        self.stackMin.append(minVal)  

    def pop(self) -> None:
        self.stackElem.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stackElem[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        
