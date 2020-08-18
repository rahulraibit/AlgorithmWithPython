import sys
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices;
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def pickminDistances(self, dist, sptset):
        min = sys.maxsize;
        for v in range(self.vertices):
            if dist[v] < min and sptset[v] == False:
                min = dist[v]
                min_index = v;
        return min_index;

    #method to implement dikstra algorithm
    def dijkstra(self, source):
        dist = [sys.maxsize]*self.vertices
        dist[source] = 0;
        sptset = [False]*self.vertices;
        for cout in range(self.vertices):
            u = self.pickminDistances(dist, sptset);
            sptset[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and sptset[v] == False and dist[v] >  self.graph[u][v] + dist[u]:
                    dist[v] =  self.graph[u][v] + dist[u]
        self.printSolution(dist)
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.vertices): 
            print (node, "\t", dist[node])

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
g.dijkstra(0); 
#g.printSolution(dist)
  

