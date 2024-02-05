from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes=set() #for vertices
        self.edges=defaultdict(list) #for edges
        self.distances={}

    def addNode(self,value):
        self.node.add(value)

    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode,toNode)]=distance

def dijkstra(graph,initial):
    visited={initial:0}
    path=defaultdict(list)

    nodes=set(graph.nodes)

    while nodes:
        minNode=None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode=node

# cont. later




        