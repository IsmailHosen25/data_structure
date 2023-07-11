class Stack:
    def __init__(self):
        self.arr = []

    def push(self, str):
        self.arr.append(str)
    def is_empty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
    def pop(self):
        if(self.is_empty==True):
            print("stuck is empty")
        else:
           return self.arr.pop()
    def peek(self):
        if(self.is_empty==True):
            print("stuck is empty")
        else:
           return self.arr[-1]
    def size(self):
        return len(self.arr)

    def print_stack(self):
        return self.arr
s=Stack()
s.push(5)
s.push(3)
s.push(7)
print(s.print_stack())
s.pop()
print(s.print_stack())
s.push(12)
print(s.print_stack())
print(s.peek())