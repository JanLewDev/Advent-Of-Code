import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle
import networkx as nx
import matplotlib.pyplot as plt


def p1():
    ans = 0
    graph = {i[:i.index(":")]: [j for j in i.replace(":", '').split()[1:]] for i in data.splitlines()}
    G = nx.Graph()
    for node in graph:
        for other in graph[node]:
            G.add_edge(node, other)  
            G.add_edge(other, node)

    # used to discover the shape of the graph
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()
    # there are also 3 edges in the min cut in the input graph
    G.remove_edges_from(nx.minimum_edge_cut(G))
    a, b = nx.connected_components(G)

    print(f"answer is {len(a) * len(b)}")
    
p1()