from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self):
        self.adj_list = {}

    def __str__(self):
        return str(self.adj_list)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    @abstractmethod
    def add_edge(self, u, v):
        pass

    @abstractmethod
    def remove_edge(self, u, v):
        pass

    def build_from(self, edges, weighted=False):
        for edge in edges:
            if weighted:
                u, v, weight = edge
                self.add_vertex(u)
                self.add_vertex(v)
                self.add_edge(u, v, weight)
            else:
                u, v = edge
                self.add_vertex(u)
                self.add_vertex(v)
                self.add_edge(u, v)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.remove_edge(vertex, neighbor)
            del self.adj_list[vertex]


class DirectedGraph(Graph):
    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].remove(v)


class UndirectedGraph(Graph):
    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)


class WeightedUndirectedGraph(Graph):
    def add_edge(self, u, v, weight=1):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u] = [edge for edge in self.adj_list[u] if edge[0] != v]
            self.adj_list[v] = [edge for edge in self.adj_list[v] if edge[0] != u]


class WeightedDirectedGraph(Graph):
    def add_edge(self, u, v, weight=1):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append((v, weight))

    def remove_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u] = [edge for edge in self.adj_list[u] if edge[0] != v]
