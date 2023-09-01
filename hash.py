# Linear Probing:
class Hashtable:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.size=0
        self.table=[None]*capacity
    def hashfunction(self,value):
        return abs(value)%self.capacity
    def insert(self,value):
        loadfactor=self.size/self.capacity
        if(loadfactor>0.6):
            self.rehash()
        hashvalue=self.hashfunction(value)
        while self.table[hashvalue] !=None:
            hashvalue=(hashvalue+1)
        self.table[hashvalue]=value
        self.size+=1
    def delete(self, value):
        hash_value = self.hashfunction(value)

        while self.table[hash_value]!=None:
            if(self.table[hash_value]==value):
               self.table[hash_value]=None
               return
            hash_value=(hash_value+1)
    def find(self,value):
        hash_value = self.hashfunction(value)
        if(self.table[hash_value]==value):
            return True
        while self.table[hash_value]!=None:
            if(self.table[hash_value]==value):
               return True
            hash_value=(hash_value+1)
        return False
    def rehash(self):
        newcapcity=self.capacity*2
        newtable=[None]*newcapcity
        self.capacity=newcapcity
        for value in self.table:
            if(value !=None):
                newHasvalue=self.hashfunction(value)
                while newtable[newHasvalue] !=None:
                    newHasvalue=(newHasvalue+1)
                newtable[newHasvalue]=value
        self.table=newtable
    def printvalue(self):
        for backet in self.table:
            print(backet)
ht=Hashtable()
ht.insert(10)
ht.insert(20)
ht.insert(11)
ht.insert(40)
ht.insert(33)
ht.insert(50)
ht.insert(60)
ht.insert(22)
ht.insert(48)
ht.printvalue()
print()
print()
ht.delete(200)
ht.delete(20)
ht.delete(33)
ht.printvalue()
