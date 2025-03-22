class Graph:
    def __init__(self, directed=False, weighted=False):
        self.adj_list = {}  # Adjacency List
        self.directed = directed
        self.weighted = weighted

    def __str__(self):
        return str(self.adj_list)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []  # Can also be a LinkedList

    def add_edge(self, u, v, weight=1):
        if u in self.adj_list and v in self.adj_list:
            if self.weighted:
                self.adj_list[u].append((v, weight))
                if not self.directed:
                    self.adj_list[v].append((u, weight))
            else:
                self.adj_list[u].append(v)
                if not self.directed:
                    self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            if self.weighted:
                self.adj_list[u] = [edge for edge in self.adj_list[u] if edge[0] != v]
                if not self.directed:
                    self.adj_list[v] = [
                        edge for edge in self.adj_list[v] if edge[0] != u
                    ]
            else:
                if v in self.adj_list[u]:
                    self.adj_list[u].remove(v)
                if not self.directed and u in self.adj_list[v]:
                    self.adj_list[v].remove(u)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in list(self.adj_list[vertex]):
                if self.weighted:
                    self.remove_edge(vertex, neighbor[0])
                else:
                    self.remove_edge(vertex, neighbor)
            del self.adj_list[vertex]
