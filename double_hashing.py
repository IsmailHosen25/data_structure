class Hashtable:
    def __init__(self,capacity=7):
          self.capacity=capacity
          self.table=[None]*capacity
          self.size=0
    def hashfunction(self,value):
         return ((2*value)+5)%self.capacity
    def sechashfunction(self,value):
         return 6-(value%6)
    def insert(self,value):
         loadfactor=self.size/self.capacity
         if(loadfactor>0.6):
              self.rehash()
         hashvalue=self.hashfunction(value)
         sechashvalue=self.sechashfunction(value)
         while self.table[hashvalue] !=None:
              hashvalue=(hashvalue+sechashvalue)%self.capacity
         self.table[hashvalue]=value
         self.size+=1
    def find(self,value):
         hashvalue=self.hashfunction(value)
         sechashvalue=self.sechashfunction(value)
         while self.table[hashvalue]!=None:
            if(self.table[hashvalue]==value):
                   print(True)
                   return
            hashvalue=(hashvalue+sechashvalue)%self.capacity
         print(False)
         return
    def delete(self,value):
         hashvalue=self.hashfunction(value)
         sechashvalue=self.sechashfunction(value)
         while self.table[hashvalue]!=None:
              if(self.table[hashvalue]==value):
                   self.table[hashvalue]=None
                   return
              hashvalue=(hashvalue+sechashvalue)%self.capacity
    def rehash(self):
         newcapacity=self.capacity*2
         newtable=[None]*newcapacity
         self.capacity=newcapacity
         for value in self.table:
                if(value!=None):
                   hashvalue=self.hashfunction(value)
                   sechashvalue=self.sechashfunction(value)
                   while newtable[hashvalue] !=None:
                        hashvalue=(hashvalue+sechashvalue)%self.capacity
                   newtable[hashvalue]=value
         self.table=newtable    
    def printHash(self):
         for value in self.table:
              print(value)
h=Hashtable()
h.insert(21)
h.insert(14)
h.insert(18)
h.insert(16)
h.printHash()
print()
print()
h.insert(397)
h.insert(42)
h.insert(321)
h.insert(90)
h.insert(387)
h.insert(45)
h.delete(21765)
h.printHash()
h.find(387)