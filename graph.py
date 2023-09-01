class Graph:
    def __init__(self,directed=True):
        self.graph=dict()
        self.directed=directed
    def addNode(self,newNode):
        if(self.graph.get(newNode) == None):
            self.graph[newNode]=[]
    
    def removeNode(self,node):
        if(self.graph.get(node)!=None):
            for x in self.graph:
                if(node in self.graph[x]):
                    self.graph[x].remove(node)
            del self.graph[node]

    def addedge(self,start,end):
        if(self.graph.get(start)==None):
            self.graph[start]=[]
        if(self.graph.get(end)==None):
            self.graph[end]=[]
        if(self.graph.get(start)!=None):
            self.graph[start].append(end)
        if(self.directed==False):
            if(self.graph.get(end)!=None):
                self.graph[end].append(start)
    def removeEdge(self,start,end):
        if(self.graph.get(start) !=None):
            if end in self.graph[start]:
                self.graph[start].remove(end)
        if(self.directed==False):
            if(self.graph.get(end)!=None):
                if(start in self.graph[end]):
                    self.graph[end].remove(start)
    def printGraph(self):
        for x in self.graph:
            print(f"{x} : {self.graph[x]}")
    def printOutdegree(self):
            for x in self.graph:
                print(f"{x} : {len(self.graph[x])}")
h=Graph()
h.addedge("A","B")
h.addedge("C","B")
h.addedge("C","A")
h.printGraph()
print()
h.printOutdegree()