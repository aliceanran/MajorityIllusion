import networkx as nx
import random


def experiences_majority_illusion(g, v):    # does node v in graph g experience majority illusion?
    active_neighbors = 0
    for n in g.adj[v]:
        if g.nodes[n]['active'] == 1:
            active_neighbors += 1
    if active_neighbors / len(g.adj[v]) >= 0.5:
        return True
    return False


def majority_illusion_count(g):     # how many nodes in graph g experience majority illusion?
    counter = 0
    for v in g.nodes:
        if experiences_majority_illusion(g, v):
            counter += 1
    return counter


"""
# old version
def mark_top_r_active(g, r):      # marks a proportion r (approximately) of top nodes in g as active
    g_by_node_degree = sorted(g.degree, key=lambda y: y[1], reverse=True)
    n_active = round(r * len(g.nodes))
    print(n_active)
    print(g_by_node_degree[n_active])
    active_min_degree = g_by_node_degree[n_active][1]
    for v in g.nodes:
        if g.degree[v] > active_min_degree:
            g.nodes[v]['active'] = 1
        else:
            g.nodes[v]['active'] = 0
"""


def mark_top_r_active(g, r):      # marks a proportion r (approximately) of top nodes in g as active
    g_by_node_degree = [v[0] for v in sorted(g.degree, key=lambda y: y[1], reverse=True)]
    n_active = round(r * len(g.nodes))
    print(g_by_node_degree[n_active])
    for j in range(n_active):
        g.nodes[g_by_node_degree[j]]['active'] = 1
    for j in range(n_active, len(g_by_node_degree)):
        g.nodes[g_by_node_degree[j]]['active'] = 0


def mark_random_r_active(g, r):     # marks a proportion r (approximately) of random nodes in g as active
    n_active = round(r * len(g.nodes))
    node_sample = random.sample(list(g.nodes), n_active)
    print(len(node_sample))
    for v in g.nodes:
        if v in node_sample:
            g.nodes[v]['active'] = 1
        else:
            g.nodes[v]['active'] = 0


for i in range(10):
    graph = nx.read_edgelist("oregon1_010505.txt", create_using=nx.DiGraph(), nodetype=int).to_undirected()
    mark_random_r_active(graph, (i+1)/20)
    print("random " + str((i+1)/20) + " nodes marked active")
    mic = majority_illusion_count(graph)
    print(str(mic) + " nodes experience majority illusion.")
    print("fraction experiencing majority illusion " + str(mic/len(graph.nodes)) + "\n")
