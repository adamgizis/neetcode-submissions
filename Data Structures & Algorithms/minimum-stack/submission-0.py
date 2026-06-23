class Node:
    def __init__(self, val, m=None):
        self.val = val
        self.m = m
class MinStack:

    def __init__(self):
        self.stack = []
        self.gmin = None
        

    def push(self, val: int) -> None:
        node = Node(val, self.gmin)
        if self.gmin is not None:
            self.gmin = min(node.val, self.gmin)
        else:
            self.gmin = node.val
        self.stack.append(node)

        

    def pop(self) -> None:
        node = self.stack.pop(-1)
        self.gmin = node.m
        
    def top(self) -> int:
        return self.stack[-1].val
        

    def getMin(self) -> int:
        return self.gmin
        
