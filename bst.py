class Node:
   def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None
class BST:
    def __init__(self):
      self.root=None
    def insert(self,value):
        if(self.root==None):
          self.root=Node(value)
          return
        par=None
        cur=self.root
        while cur !=None:
            par=cur
            if(value<cur.data):
              cur=cur.left
            else:
              cur=cur.right
        newNode=Node(value)
        if(value<par.data):
           par.left=newNode
        else:
           par.right=newNode
    def find(self,value):
        if(self.root==None):
          print("Bst is empty")
          return
        cur=self.root
        while cur!=None:
            if(cur.data==value):
              return True
            if(value<cur.data):
               cur=cur.left
            else:
               cur=cur.right
        return False
    def remove(self, value):
        if(self.root==None):
          print("bst is empty")
          return
        par=None
        cur=self.root
        while cur != None:
            if(cur.data==value):
              break
            par=cur
            if(value<cur.data):
               cur=cur.left
            else:
               cur=cur.right
        if(cur==None):
           print("Value is not Found")
           return
        if(cur.left==None and cur.right==None):
            if(par.left==cur):
              par.left=None
            else:
              par.right=None
        elif(cur.left==None or cur.right==None):
            child=cur.left
            if(child==None):
              child=cur.right
            if(cur==par.left):
               par.left=child
            else:
               par.right=child
        else:
            par = cur
            suc = cur.right
            while suc.left is not None:
              par = suc
              suc = suc.left
            child = suc.right
            if suc is par.left:
               par.left = child
            else:
               par.right = child
            cur.data=suc.data
s=BST()
s.insert(10)
s.insert(20)
s.insert(5)
s.insert(6)
s.insert(35)
s.insert(1)
print(s.find(20))
s.remove(6)
print(s.find(6))