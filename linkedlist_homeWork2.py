class Node:
    def __init__(self,value):
       self.data=value
       self.next=None
class SLL:
    def __init__(self,):
         self.head=None
    def add_data(self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
        else:
            cur=self.head
            while cur!=None:
                if(cur.next==None):
                    cur.next=new_node
                    break
                else:
                    cur=cur.next
    def insert(self,index,value):
        i=0
        new_node=Node(value)
        if(index==0):
            new_node.next=self.head
            self.head=new_node
        else:
            cur=self.head
            while cur!=None:
              if(i==index-1):
                new_node.next=cur.next
                cur.next=new_node
                break
            cur=cur.next
            i=i+1
            if(cur==None):
                print(f"Eror: index out of range {index}")
    def add_befor_head(self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
        else:
           new_node.next=self.head
           self.head=new_node
    def sll_print(self):
        cur=self.head
        print("",end="Head -> ")     
        while cur.next!=None:
            print(cur.data,end=" -> ")
            cur=cur.next
        print(cur.data,"-> None")
l=SLL()
l.add_data(5)
l.add_data(10)
l.add_data(20)
l.add_befor_head(45)
l.add_befor_head(50)
l.insert(4,70)
l.sll_print()