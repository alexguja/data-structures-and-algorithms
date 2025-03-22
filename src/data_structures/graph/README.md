## Graphs

Graphs are a data structure that consists of a finite set of vertices (nodes) and a collection of edges that connect pairs of vertices. Graphs are used to represent networks. The edges may be directed or undirected.

We can choose between two standard ways to represent a graph $G = (V, E)$
as a collection of *adjacency lists* or as an *adjacency matrix*. Either way applies
to both directed and undirected graphs.

Because the adjacency-list representation
provides a compact way to represent sparse graphs, those for which $|E| << |V|^2$ 
is usually the method of choice.

We may prefer an adjacency-matrix representation, however, when the
graph is dense $|E| \approx |V|^2$  or when we need to be able to tell quickly
if there is an edge connecting two given vertices.