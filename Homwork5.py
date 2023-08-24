import random
class Node:
    def __init__(self,value):
        self.data=value
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if(self.root==None):
            self.root=Node(value)
            return
        cur=self.root
        par=None
        while cur!=None:
            par=cur
            if(cur.data<value):
                cur=cur.right
            else:
                cur=cur.left
        if(par.data<value):
            par.right=Node(value)
        else:
            par.left=Node(value)

    #Q2
    def insertR(self,value):
        if(self.root==None):
            self.root=Node(value)
            return
        return helperinsertR(self.root,value)


    #Q3
    def maxBst(self,root):
        if(root==None):
            print("Bst is empthy")
            return
        if(root.right==None):
            print("Max: ",root.data)
            return
        self.maxBst(root.right)  


    #Q4
    def minBst(self,root):
        if(root==None):
            print("Bst is empty")
            return
        if(root.left==None):
           print("Min: ",root.data)
           return
        self.minBst(root.left)


    #Q5
    # def searchR(self,root,data):
    #     if(root.data==data):
    #         return True
    #     self.searchR(root.left,data)
    #     self.searchR(root.right,data)
    #     return False
          
def helperinsertR(cur,value):
    if(cur.data<value):
        if(cur.right==None):
            cur.right=Node(value)
            return 
        helperinsertR(cur.right,value)
    else:
        if(cur.left==None):
            cur.left=Node(value)
            return 
        helperinsertR(cur.left,value)
def inorder(s):
    if(s==None):
        return
    inorder(s.left)
    print(s.data,end=" ")
    inorder(s.right)


#Q1
l=[]
for i in range(1,13):
    l.append(random.randint(1,100))
s=BST()
for i in range(len(l)):
    s.insertR(l[i])
inorder(s.root)
print()
s.maxBst(s.root)
s.minBst(s.root)
s.searchR(s.root,l[3])