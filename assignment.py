#Q1
# def helper(a,b,num,num2):
#     if(a==b):
#          print(a)
#          return
#     if(a<num):
#         print(a,end=" > ")
#         helper(a+1,b,num,num2)
#     else:
#         if(a<num2):
#             print(a,end=" -- ")
#             helper(a+1,b,num,num2)
#         else:
#             print(a,end=" < ")
#             helper(a+1,b,num,num2)
# def printRange(a,b):
#         if(a>b):
#            print("error")
#            return
#         num=0
#         num2=0
#         if((a+b)%2==0):
#            num=(a+b)//2
#         else:
#             num=(a+b)//2
#             num2=num+1
#         helper(a,b,num,num2)      
# printRange(13,14)

#Q-2
# def collapseSequences(a,b):
#     if len(a)==0:
#         return ""
    
#     if len(a)==1:
#         return a
    
#     if a[0]==b and a[1]==b:
#         return collapseSequences(a[1:], b)
#     else:
#         return a[0] + collapseSequences(a[1:], b)
# print(collapseSequences("aabaaccaaaaaada", 'a'))
# print(collapseSequences("mississssipppi", 's'))
# print(collapseSequences("tennessee", 'x'))
# Q3
class Node:
   def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,v):
        if(self.root==None):
          newNode=Node(v)
          self.root=newNode
          return
        cur=self.root
        pra=None
        while cur !=None:
            pra=cur
            if(cur.data<v):
               cur=cur.right
            else:
                cur=cur.left
        newNode=Node(v)
        if(pra.data>v):
            pra.left=newNode
        else:
            pra.right=newNode
    def find(self, v):
        if(self.root==None):
            print("BST is empty")
            return
        cur=self.root
        while cur !=None:
            if(cur.data==v):
                return True
            if(cur.data<v):
                cur=cur.right
            else:
                cur=cur.left
        return False
    
#Q4
# def count(cur):
#     if(cur==None):
#         return 0
#     c=0
#     if(cur.left!=None):
#        c=c+1
#     if(cur.right!=None):
#         c=c+1
#     return count(cur.left)+count(cur.right) +c
# def numOfDescendants(root):
#     a=count(root)
#     b=count(root.left)
#     c=count(root.right)
#     d=count(root.left.left)
#     e=count(root.left.right)
#     f=count(root.left.right.left)
#     print(f"A has {a} descendants")
#     print(f"B has {b} descendants")
#     print(f"C has {c} descendants")
#     print(f"D has {d} descendants")
#     print(f"E has {e} descendants")
#     print(f"F has {f} descendants")
# def countLeftNodes(root):
#     if root is None:
#         return 0
#     c=0
#     if(root.left!=None):
#         c=1
#     return countLeftNodes(root.left) + countLeftNodes(root.right) + c
# def predecessorAndSuccessor(root,n):
#     successor=None
#     predecessor=None
#     cur=root.left
#     while cur!=None:
#       predecessor=cur.data
#       cur=cur.right
#     cur=root.right
#     while cur!=None:
#         successor=cur.data
#         cur=cur.left
#     print(f"The predecessor of {n} is {predecessor} and the successor is {successor}.")

# s=BST()
# s.insert(7)
# s.insert(4)
# s.insert(8)
# s.insert(6)
# s.insert(3)
# s.insert(5)
# numOfDescendants(s.root)
#Q5
# def countLeftNodes(root):
#     cur=root
#     if(cur==None):
#         return 0
#     if(cur!=None):
#         par=cur
#         return 1 +countLeftNodes(cur.left)
#     return 1 +countLeftNodes(par.right.left)
# print(countLeftNodes(s.root))
# predecessorAndSuccessor(s.root,10)