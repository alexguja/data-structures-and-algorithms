from data_structures.stack.stack import Stack


def dfs(graph):
    parent_vertices = {}
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            parent_vertices[vertex] = None
            dfs_visit(graph, vertex, visited, parent_vertices)

    return parent_vertices


def dfs_visit(graph, start_vertex, visited, parent_vertices):
    visited.add(start_vertex)
    for neighbour in graph[start_vertex]:
        if neighbour not in visited:
            parent_vertices[neighbour] = start_vertex
            dfs_visit(graph, neighbour, visited, parent_vertices)


def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = Stack()  # LIFO data structure

    stack.push(start_vertex)
    visited.add(start_vertex)

    while stack:
        current_vertex = stack.pop()
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.push(neighbour)

    return visited
