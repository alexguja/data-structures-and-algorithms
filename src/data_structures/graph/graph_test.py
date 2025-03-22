from data_structures.graph.graph import DirectedGraph
from data_structures.graph.graph import UndirectedGraph


def test_directed_graph():
    graph = DirectedGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")

    assert "A" in graph.adj_list
    assert "B" in graph.adj_list
    assert "B" in graph.adj_list["A"]
    assert "A" not in graph.adj_list["B"]

    graph.remove_edge("A", "B")
    assert "B" not in graph.adj_list["A"]

    graph.remove_vertex("A")
    assert "A" not in graph.adj_list


def test_undirected_graph():
    graph = UndirectedGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")

    assert "A" in graph.adj_list
    assert "B" in graph.adj_list
    assert "B" in graph.adj_list["A"]
    assert "A" in graph.adj_list["B"]

    graph.remove_edge("A", "B")
    assert "B" not in graph.adj_list["A"]
    assert "A" not in graph.adj_list["B"]

    graph.remove_vertex("A")
    assert "A" not in graph.adj_list
