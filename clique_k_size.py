from itertools import combinations
import networkx as nx


def k_cliques(graph):
    # 2-cliques
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 2

    while cliques:
        # result
        yield k, cliques

        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u, v in combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1


def print_cliques(graph, size_k):
    for k, cliques in k_cliques(graph):
        if k == size_k:
            print('%d-cliques = %d, %s.' % (k, len(cliques), cliques))


nodes, edges = 6, 10
size_k = 3
graph = nx.Graph()
graph.add_nodes_from(range(nodes))
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 5)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(3, 6)
graph.add_edge(4, 5)
graph.add_edge(4, 6)

print_cliques(graph, size_k)