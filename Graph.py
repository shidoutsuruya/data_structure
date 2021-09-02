class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def __str__(self):
        return str(self.id)+" connectedTo:"+str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key):
        self.numVertices+=1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],weight)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
  
class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[] 
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
def buildGraph(wordFile):
    d={}
    g=Graph()
    wfile=open(wordFile)
    for line in wfile:
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
    
def dfs()