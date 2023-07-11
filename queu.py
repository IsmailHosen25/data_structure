class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)
    def is_empty(self):
        if(len(self.arr)==0):
            return True
        else:
            return False
    def dequeue(self):
        if(self.is_empty()==True):
            print("Queu is empty")
        else:
           return self.arr.pop(0)
    def peek(self):
        if(self.is_empty()==True):
            print("Queu is empty")
        else:
           return self.arr[0]
    def print_queue(self):
        return self.arr
q = Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(3)
q.enqueue(5)
print(q.print_queue())
q.dequeue()
q.dequeue()
print(q.print_queue())
print(q.peek())

