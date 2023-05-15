class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = []
        for i in range(V):
            self.adj.append([])

    def addEdge(self, v, w):
        self.adj[v].append(w)
