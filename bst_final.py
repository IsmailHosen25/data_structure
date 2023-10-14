class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def addnode(self,data):
        if(self.root==None):
            self.root=Node(data)
            return
        cur=self.root
        par=None
        while cur!=None:
            par=cur
            if(cur.data<data):
                cur=cur.right
            else:
                cur=cur.left
        if(par.data<data):
            par.right=Node(data)
        else:
            par.left=Node(data)
    def removeNode(self,data):
        if(self.root==None):
            print("BST is empty")
            return
        cur=self.root
        par=None
        while cur!=None:
            if(cur.data==data):
                break
            par=cur
            if(cur.data<data):
                cur=cur.right
            else:
                cur=cur.left

        if(cur==None):
            print("Not Found")
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
            if(par.left==cur):
                par.left=child
            else:
                par.right=child
        else:
            par=cur
            suc=cur.right
            while suc.left !=None:
                par=suc
                suc=suc.left
            child=suc.right
            if(par.left==suc):
                par.left=child
            else:
                par.right=child
            cur.data=suc.data
def inorder(cur):
        if(cur==None):
            return
        inorder(cur.left)
        print(cur.data,end=" ")
        inorder(cur.right)
#Q1
def printLevelWiseNodes(root):
    ans=[]
    if(root==None):
        print("None")
        return ans
    queue=[]
    queue.append(root)
    while queue:
        currentlist=[]
        currentlist_size=len(queue)
        while currentlist_size>0:
            currentNode=queue.pop(0)
            currentlist.append(currentNode.data)
            currentlist_size-=1

            if(currentNode.left):
                queue.append(currentNode.left)
            if(currentNode.right):
                queue.append(currentNode.right)
        ans.append(currentlist)
    return ans

#Q2
def levelmexbst(root):
    c=printLevelWiseNodes(root)
    d=[]
    for i in c:
        d.append(i.pop())
    return d


#Q4
def isDuplicate(root1, root2):
  if(root1==None and root2==None):
      return True
  elif(root1!=None and root2==None):
      return False
  elif(root1==None and root2!=None):
      return False
  else:
      return (root1.data == root2.data) and (isDuplicate(root1.left,root2.left)) and (isDuplicate(root1.right,root2.right))


#Q8

def countNodes(root):
    if(root==None):
        return 0
    return 1+ countNodes(root.left)+countNodes(root.right)

h=BST()
h.addnode(7)
h.addnode(8)
h.addnode(3)
h.addnode(90)
h.addnode(1)
h.addnode(5)
inorder(h.root)
k=printLevelWiseNodes(h.root)
print()
for i in k:
    for j in i:
       print(j,end=" ")
    print()

l=levelmexbst(h.root)
for i in l:
    print(i)

print()
print()
print(countNodes(h.root))

s=BST()
s.addnode(7)
s.addnode(8)
s.addnode(3)
s.addnode(9)
s.addnode(1)
s.addnode(5)
print(isDuplicate(s.root,h.root))