class MinStack:

    def __init__(self):
       self.stack_list = []

    def push(self, val: int) -> None:
        return self.stack_list.insert(0,val)
        

    def pop(self) -> None:
        return self.stack_list.pop(0)

    def top(self) -> int:
        return self.stack_list[0]

    def getMin(self) -> int:
        return min(self.stack_list)
        
