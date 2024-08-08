from data_structures.queue import Queue

def bfs(graph, start_vertex):
    visited = set()
    queue = Queue() # FIFO data structure

    queue.enqueue(start_vertex)
    visited.add(start_vertex)

    while queue:
        current_vertex = queue.dequeue()
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.enqueue(neighbour)
    
    return visited