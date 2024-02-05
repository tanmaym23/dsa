class Graph:
    def __init__(self,gdict=None):
        if gdict==None:
            gdict={}
        self.gdict=gdict
    
    def addEdge(self,edge,vertex):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            devertex=queue.pop(0)
            print(devertex)
            for adjacentvertex in self.gdict[devertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)
    
    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popVertex=stack.pop()
            print(popVertex)
            for adjacentvertex in self.gdict[popVertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)

customDict={
    "a":["b","c"],
    "b":["a","d","e"],
    "c":["a","e"],
    "d":["b","e","f"],
    "e":["d","f","c"],
    "f":["d","e"],
}

graph=Graph(customDict)
# print(graph.gdict)
# graph.addEdge("e","b")
# print(graph.gdict)
# graph.bfs("a")
graph.dfs("a")
