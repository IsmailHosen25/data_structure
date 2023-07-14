##################### Q-1

# results_list = [[1234111, 'A', 73],
# [1234222, 'W', 17],
# [1234333, 'W', 57],
# [1234444, 'A', 89],
# [1234555, 'A', 32]]
# ######## a
# def grade(n):
#     if(n>=80 and n<=100):
#         return "A"
#     elif(n<=79 and n>=60 ):
#         return "B"
#     elif(n<=59 and n>=40):
#         return "C"
#     elif(n<=39 and n>=0):
#         return "F"
#     else:
#         return 
# ######## b
# for i in range(len(results_list)):
#     if(results_list[i][1]!="W"):
#         print(f"{results_list[i][0]} {grade(results_list[i][2])}")
#     else:
#         print(f"{results_list[i][0]} {results_list[i][1]}")
# ####### c
# t=[]
# for i in range(len(results_list)):
#     if(results_list[i][1]!="W"):
#            t.append(results_list[i])
# for i in range(len(results_list)):
#     results_list.pop()
# while (len(t)) !=0:
#     results_list.append(t.pop())
# for i in range(len(results_list)-1,-1,-1):
#     print(f"{results_list[i][0]} {grade(results_list[i][2])}")

###################### Q-2
 
#### a
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, str):
        self.arr.append(str)
    def pop(self):
           return self.arr.pop()
    def size(self):
        return len(self.arr)
    def display(self):
         print(self.arr)
# s1=Stack()
# s1.push("D")
# s1.push("C")
# s1.push("B")
# s1.push("A")
# s1.display()
# s2=Stack()
# s3=Stack()
# s2.push(s1.pop())
# s2.push(s1.pop())
# s3.push(s1.pop())
# s3.push(s1.pop())
# s3.push(s2.pop())
# s3.push(s2.pop())
# s3.display()

#### b
class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)
    def dequeue(self):
           return self.arr.pop(0)
    def size(self):
         return len(self.arr)
    def print_queue(self):
        print(self.arr)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)
def reverseK(q, k):
        t_k=q.size()-k
        t=Stack()
        for i in range(k):
            t.push(q.dequeue())
        for i in range(t.size()):
             q.enqueue(t.pop())
        for i in range(t_k):
             q.enqueue(q.dequeue())
reverseK(q,4)
q.print_queue()