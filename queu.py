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
    
###### Q-6
# q = Queue()
# q.enqueue(7)
# q.enqueue(8)
# q.enqueue(3)
# q.enqueue(5)
# q.enqueue(9)
# q.enqueue(3)
# q.enqueue(5)
# q.enqueue(10)
# print(q.print_queue())
# class Stack:
#     def __init__(self):
#         self.arr = []

#     def push(self, str):
#         self.arr.append(str)
#     def is_empty(self):
#         if(len(self.arr)==0):
#             return True
#         else:
#             return False
#     def pop(self):
#         if(self.is_empty==True):
#             print("stuck is empty")
#         else:
#            return self.arr.pop()

# k=int(input())
# h=Stack()
# for i in range(k):
#     h.push(q.dequeue())
# while h.is_empty() !=True:
#     q.enqueue(h.pop())
# print(q.print_queue())


id_m=list(map(int,input().split()))
A=Queue()
B=Queue()
def ech(id_m,A,B):
    for i in range(len(id_m)):
      if(id_m[i]%2==0):
            A.enqueue(id_m[i])
      else:
            B.enqueue(id_m[i])
ech(id_m,A,B)
print(A.print_queue())
print(B.print_queue())