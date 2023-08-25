#Q1
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
def inorder(cur):
    if(cur==None):
        return
    inorder(cur.left)
    print(cur.data,end=" ")
    inorder(cur.right)
def eachLevelmax(cur):
    if(cur==None):
        return
    print(cur.data)
    eachLevelmax(cur.right)
s=BST()
s.insert(10)
s.insert(5)
s.insert(13)
s.insert(7)
s.insert(3)
inorder(s.root)
print()
eachLevelmax(s.root)