from collections import defaultdict;

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v);
    def DFSUtil(self, v, visited):
        visited[v] = True;
        print(v, end=" ");
        for i in self.graph:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, s):
        visited = [False]*(len(self.graph));
         #for i in range(V):  In case of disconnected
         #   if visited[i] == False: 
         #       self.DFSUtil(i, visited) 
        self.DFSUtil(s, visited);

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2) 
  