class HashTable:
    def __init__(self,capacity=11):
        self.capacity=capacity
        self.table=[None]*capacity
        self.size=0
    def hashFunction(self,value):
        return value//self.capacity
    def insert(self,value):
            loadfactor=self.size/self.capacity
            if(loadfactor>0.6):
                 self.rehash()
            hashvalue=self.hashFunction(value)
            i=0
            while self.table[hashvalue] !=None:
                i+=1
                hashvalue=(self.hashFunction(value) + (i*i))//self.capacity
            self.table[hashvalue]=value
            self.size+=1
    def delete(self,value):
         hashvalue=self.hashFunction(value)
         i=0
         while self.table[hashvalue]!=None:
              if(self.table[hashvalue]==value):
                   self.table[hashvalue]=None
                   self.size-=1
                   return
              i+=1
              hashvalue=(self.hashFunction(value) +(i*i))//self.capacity
    def find(self,value):
         hashvalue=self.hashFunction(value)
         i=0
         while self.table[hashvalue] !=None:
              if(self.table[hashvalue]==value):
                   print(True)
                   return 
              i+=1
              hashvalue=(self.hashFunction(value)+(i*i))//self.capacity
         print(False)
         return 
    def rehash(self):
         newcapacity=self.capacity*2
         newtable=[None]*newcapacity
         self.capacity=newcapacity
         for value in self.table:
              if(value!=None):
                    hashvalue=self.hashFunction(value)
                    i=0
                    while newtable[hashvalue]!=None:
                        i+=1
                        hashvalue=(self.hashFunction(value)+(i*i))//self.capacity
                    newtable[hashvalue]=value
         self.table=newtable
    def printhash(self):
        for value in self.table:
            print(value)
h=HashTable()
h.insert(70)
h.insert(31)
h.insert(58)
h.insert(8)
h.insert(102)
h.insert(68)
h.insert(25)
h.printhash()