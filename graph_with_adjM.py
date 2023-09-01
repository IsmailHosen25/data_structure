class Graph:
    def __init__(self, directed):
        self.graph={}
        self.directed=directed
    def addNode(self,newnode):
        self.graph[newnode]={}
        for i in self.graph:
            self.graph[newnode][i]=0
        for i in self.graph:
            self.graph[i][newnode]=0
    def removeNode(self,node):
        self.graph.pop(node)
        for i in self.graph:
            self.graph[i].pop(node)
    def addedge(self,start,end):
        if(start not in self.graph):
            self.graph[start]={}
            for i in self.graph:
                self.graph[start][i]=0
            for i in self.graph:
                self.graph[i][start]=0
        if(end not in self.graph):
            self.graph[end]={}
            for i in self.graph:
                self.graph[end][i]=0
            for i in self.graph:
                self.graph[i][end]=0
        
        self.graph[start][end]=1
        if(self.directed==False):
            self.graph[end][start]=1
    def removedge(self,start,end):
        self.graph[start][end]=0
        if(self.directed==False):
           self.graph[end][start]=0
    def printgraph(self):
        for x in self.graph:
            print(f"{x} : {self.graph[x]}")
    def maxoutdegree(self):
        c=0
        v=0
        for x in self.graph:
            q=0
            for i in self.graph[x]:
                if(self.graph[x][i]==1):
                    q+=1
            if(q>=c):
                c=q
                v=x
        print(f"Max outdegree: {v}: {self.graph[v]} ")
    def maxindegree(self):
        c=0
        v=0
        for i in self.graph:
            q=0
            for x in self.graph:
                if(self.graph[x][i]==1):
                    q+=1
            if(q>=c):
                c=q
                v=i
        print(f"Max indegree: {v} : {c}")
    def sinkNode(self):
        c=0
        v=0
        for i in self.graph:
            q=0
            for x in self.graph[i]:
                if(self.graph[i][x]==0):
                    q+=1
            if(c<=q):
               c=q
               v=i
        print(f'Sink Node: {v}: {self.graph[v]}')

h=Graph(True)
h.addNode(10)
h.addNode(12)
h.addNode(1)
h.addedge(10,1)
h.addedge(10,12)
h.addedge(10,3)
h.addedge(3,12)
h.addedge(1,3)
h.addedge(1,12)
h.addedge(1,10)
h.printgraph()
h.maxoutdegree()
h.maxindegree()
h.sinkNode()
