class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
class sgll:
    def __init__(self):
      self.head=None
      self.till=None
      self.size=0
    def append(self,value):
        newNode=Node(value)
        if(self.head==None ):
           self.head=newNode
           self.till=newNode
           self.size+=1
        else:
           self.till.next=newNode
           self.till=newNode
           self.size+=1
    def add_first(self,value):
        newNode=Node(value)
        if(self.head==None):
           self.head=newNode;
           self.till=newNode
           self.size+=1
        else:
           newNode.next=self.head
           self.head=newNode
           self.size+=1
    def insrt_after_x(self,x,value):
       newNode=Node(value)
       if(self.head==None):
          self.head=newNode
          self.till=newNode
          self.size+=1
       else:
            if(self.till.value==x):
               self.append(value)
            else:
               current=self.head
               while current.next!=None:
                 if(current.value==x):
                    newNode.next=current.next
                    current.next=newNode
                    self.size+=1
                    break
                 else:
                   current=current.next
    def insert_befor_x(self,x,value):
        newNode=Node(value)
        if(self.head==None):
           self.head=newNode
           self.till=newNode
           self.size+=1
        else:
            if(self.head.value==x):
                   self.add_first(value)
            else:
               current=self.head
               while current.next!=None:
                  if(current.next.value==x):
                     newNode.next=current.next
                     current.next=newNode
                     self.size+=1
                     break
                  else:
                    current=current.next
    def pop(self):
       current=self.head
       while current.next!=None:
            if(current.next.next==None):
               current.next=None
               self.till=current
               self.size-=1
               break
            else:
               current=current.next
               
    def remove_first(self):
       self.head=self.head.next
       self.size-=1
    def remove_x(self,x):
        if(self.head.value==x):
           self.remove_first()
        elif(self.till.value==x):
           self.pop()
        else:
           current=self.head
           while current.next!=None:
             if(current.next.value==x):
               current.next=current.next.next
               self.size-=1
               break
             else:
               current=current.next
    def size_sgll(self):
       return self.size
    def print_sgll(self):
        if(self.head==None):
           print("linked list is empty")
        else:
            current=self.head
            print("Head -> ",end="")
            while current.next != None:
                print(current.value,end=" -> ")
                current=current.next
            print(current.value,end=" -> None")
            
s=sgll()

print(s.size_sgll(),end=" - Singly linked list size.\n")
s.print_sgll()
s.append(3)
s.append(8)
s.append(4)
s.append(3)
s.append(16)
s.insert_befor_x(3,2)
print(s.size_sgll(),end=" - Size\n")
s.print_sgll()

        