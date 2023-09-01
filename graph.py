class Graph:
    def __init__(self,directed=True):
        self.graph={}
        self.directed=directed
    def addNode(self,node):
        if(node not in self.graph):
            self.graph[node]=[]
            return
    def removeNode(self,node):
        if(node not in self.graph):
            print("Not Found")
            return
        for i in self.graph:
            if(node in self.graph[i]):
                self.graph[i].remove(node)
        self.graph.pop(node)
    def addedge(self,start,end):
        if(start not in self.graph):
            self.graph[start]=[]
        if(end not in self.graph):
            self.graph[end]=[]
        self.graph[start].append(end)
        if(self.directed==False):
            self.graph[end].append(start)
    def removeedge(self,start,end):
        if(start not in self.graph):
            print("Not Found")
            return
        self.graph[start].remove(end)
        if(self.directed==False):
            self.graph[end].remove(start)
    def printgraph(self):
        for i in self.graph:
          print(f"{i} : {self.graph[i]}")

    def printoutdegree(self):
        for i in self.graph:
            print(f"Out Degree of  {i}  is {len(self.graph[i])}")

    def printInDegree(self):
     for x in self.graph:
        c=0
        for k in self.graph:
           if(x in self.graph[k]):
               c+=1
        print(f"In Degree of {x} is {c}")
    def maxoutdegree(self):
        c=0
        v=[0]
        for x in self.graph:
            if(len(self.graph[x])>=c):
               c=len(self.graph[x])
               v.pop()
               v.append(x)
        print(f"Max Out Degree Nodes : {v}")
    def maxindegree(self):
        c=0
        v=[0]
        for x in self.graph:
            q=0
            for k in self.graph:
                if(x in self.graph[k]):
                    q+=1
            if(q>c):
                c=q
                v.pop()
                v.append(x)
        print(f"Max In Degree Nodes : {v}")
    def printSinkNodes(self):
        c=[]
        for x in self.graph:
            if(len(self.graph[x])==0):
                c.append(x)
        print('Sink Nodes :',c)
h=Graph(True)
h.addedge('A','C')
h.addedge('A','B')
h.addedge('A','D')
h.addedge('B','C')
h.addedge('B','E')
h.addedge('E','E')
h.addedge('E','D')
h.addedge('D','C')
h.printgraph()
print()
print()
h.printoutdegree()
h.printInDegree()
h.maxindegree()
h.maxoutdegree()
h.printSinkNodes()
