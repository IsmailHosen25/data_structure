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

##### Q-1
# str_input=input()
# def reverseString(str):
#   helperStack = Stack()
#   for i in range(len(str)):
#     helperStack.push(str[i])
#   rev=''
#   while helperStack.is_empty() !=True:
#     char=helperStack.peek()
#     rev+=char
#     helperStack.pop()
#   return rev
# a= 'hello how are you doing'
# print(reverseString(str_input))

########### Q-2

###### Q-3

# top=Stack()
# top.push(23)
# top.push(53)
# top.push(56)
# top.push(19)
# top.push(94)
# top.push(22)
# top.push(89)
# top.push(44)
# print(top.print_stack())
# def leargest(top):
#     max=top.peek()
#     hlp=Stack()
#     while top.is_empty() != True:
#         a=top.peek()
#         if(max<a):
#             max=a
#         hlp.push(a)
#         top.pop()
#     while hlp.is_empty()!=True:
#         a=hlp.peek()
#         if(a!=max):
#             top.push(a)
#         hlp.pop()
#     top.push(max)
#     return top
# print(leargest(top).print_stack())

################ Q-4
# s1=Stack()
# s1.push(1)
# s1.push(5)
# s1.push(11)
# s1.push(4)
# print(s1.print_stack())
# s2=Stack()
# s2.push(4)
# s2.push(32)
# s2.push(1)
# s2.push(-1)
# print(s2.print_stack())
# def baleance_stack(s1,s2):
#     s1_hlp=Stack()
#     s2_hlp=Stack()
#     s1_sum=0
#     s2_sum=0
#     while(s1.is_empty()!=True):
#         s1_sum+=s1.peek()
#         s1_hlp.push(s1.pop())
#     while (s2.is_empty()!=True):
#         s2_sum+=s2.peek()
#         s2_hlp.push(s2.pop())
#     while s1_hlp.is_empty() !=True:
#         s1.push(s1_hlp.pop())
#     while s2_hlp.is_empty() !=True:
#         s2.push(s2_hlp.pop())
#     baleane=s1_sum-s2_sum
#     return baleane
# s2.push(baleance_stack(s1,s2))
# print(s2.print_stack())
