class Hashtable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.table=[None]*capacity
        self.size=0
    def hashfunction(self,c):
        return ord(c)%self.capacity
    def insert(self,c):
        loadfactor=self.size/self.capacity
        if(loadfactor>0.6):
            self.rehash()
        hashvalue=self.hashfunction(c)
        if(self.table[hashvalue]==None):
            self.table[hashvalue]=[c]
            self.size+=1
        else:
            self.table[hashvalue].append(c)
            self.size+=1
    def delete(self,c):
        hashvalue=self.hashfunction(c)
        if(self.table[hashvalue]!=None and c in self.table[hashvalue]):
            self.table[hashvalue].remove(c)
            self.size-=1
            return
    def find(self,c):
        hashvalue=self.hashfunction(c)
        if(self.table[hashvalue]!=None and c in self.table[hashvalue]):
            print(True)
            return
        print(False)
        return
    def rehash(self):
        newCapacity=self.capacity*2
        newtable=[None]*newCapacity
        self.capacity=newCapacity
        for c in self.table:
             if(c!=None):
                 for k in c:
                   hashvalue=self.hashfunction(k)
                   if(newtable[hashvalue]==None):
                     newtable[hashvalue]=[k]
                   else:
                     newtable[hashvalue].append(k)
        self.table=newtable
    def printhash(self):
        for i in self.table:
            print(i)
capacity=7
h=Hashtable(capacity)
h.insert("a")
h.insert("b")
h.insert("c")
h.insert("d")
h.insert("k")
h.insert("m")
h.insert("p")
h.insert("n")
h.insert("o")
h.insert("r")
h.printhash()
h.insert("p")
h.insert("n")
h.insert("p")
print()
print()
h.delete("p")
h.printhash()
