#1 


# def sum(n):
#     if(n<=0):
#         return 0
#     sm=n+sum(n-1)
#     return sm
# print(sum(5))


#2
# def strcheck(str,l,e):
#     if(l==e):
#         return True
#     if(str[l]!=str[e]):
#         return False
#     if(l<e+1):
#         return strcheck(str, l+1,e-1)
#     return True
# def isPalindrom(str):
#     n=len(str)

#     if(n==0):
#         return True
#     return strcheck(str, 0,n-1)

# print(isPalindrom("max"))


#3

# import math
# def ispalindromnumber(num):
#     return int(num!=0) and ((num%10)+(10**int(math.log(num,10))))+ispalindromnumber(num//10)

# ch=12321
# res=ch==ispalindromnumber(ch)
# print(str(res))


#4
# def gcd(a,b):
#     if(b==0):
#         return a
#     if(a==0):
#         return b
#     if(a>b):
#         return gcd(a-b,b)
#     return gcd(a,b-a)
# print(gcd(10,15))

#5
# def reverse(string):
#     if len(string) == 0:
#         return 
#     temp = string[0]
#     reverse(string[1:])
#     print(temp, end='')
# reverse("hasan")


#6
# class Node:
#     def __init__(self,value):
#        self.data=value
#        self.next=None
# class SLL:
#     def __init__(self,):
#          self.head=None
#     def add_data(self,value):
#         new_node=Node(value)
#         if(self.head==None):
#             self.head=new_node
#         else:
#             cur=self.head
#             while cur!=None:
#                 if(cur.next==None):
#                     cur.next=new_node
#                     break
#                 else:
#                     cur=cur.next
#     def sll_print(self):
#         print("",end="Head -> ")     
#         ssll_r_print(self.head)
#         print("None")
#     def delete_k(self,k):
#         if(self.head.data==k):
#             self.head=self.head.next
#         else:
#             delete_k_nodes(self.head,k)
# def ssll_r_print(s):
#     if(s==None):
#         return 
#     print(s.data,end="->")
#     return ssll_r_print(s.next)
# def delete_k_nodes(s,k,nk=None):
#     n=s
#     if(s.data==k):
#         nk.next=s.next
#         return
#     if(s.data!=k):
#         if(s.next==None):
#             print("Not found")
#         else:
#             delete_k_nodes(s.next,k,n)

# h=SLL()
# h.add_data(1)
# h.add_data(2)
# h.add_data(3)
# h.add_data(4)
# h.add_data(5)
# h.sll_print()
# h.alt_node()

# def recursion(n):
#   if n > 0:
#     print(n - 1, end = ' ')
#     recursion(n - 1)
#     recursion(n - 2)
# recursion(4)
# def factorial(n):
#     if(n<=1):
#         return 
#     factorial(n-2)
#     factorial(n-1)
#     print(n,end=" ")
# factorial(5)