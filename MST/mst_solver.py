import numpy as np
import networkx as nx

def mst_path(points):
    # add node to the graph
    G = nx.Graph()
    for i, point in enumerate(points):
        G.add_node(i)

    # compute MST
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = np.linalg.norm(points[i]-points[j])
            edges.append((i, j, dist))
    edges.sort(key=lambda x: x[2])

    # add edges of MST
    for edge in edges:
        if not nx.has_path(G, edge[0], edge[1]):
            G.add_edge(edge[0], edge[1], length=edge[2])

    # preorder traversal
    visited = set()
    stack = [0]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(list(G.neighbors(node))):
                stack.append(neighbor)

    return order