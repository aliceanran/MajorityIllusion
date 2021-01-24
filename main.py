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


def mark_top_r_active(g, r):      # marks a proportion r (approximately) of top nodes in g as active
    g_by_node_degree = sorted(g.degree, key=lambda y: y[1], reverse=True)
    n_active = round(r * len(g.nodes))
    active_min_degree = g_by_node_degree[n_active]
    for v in g.nodes:
        if g.degree[v] > active_min_degree:
            g.nodes[v]['active'] = 1
        else:
            g.nodes[v]['active'] = 0


def mark_random_r_active(g, r):     # marks a proportion r (approximately) of random nodes in g as active
    n_active = round(r * len(g.nodes))
    node_sample = random.sample(g.nodes, n_active)
    for v in g.nodes:
        if v in node_sample:
            g.nodes[v]['active'] = 1
        else:
            g.nodes[v]['active'] = 0


graph = nx.read_edgelist("oregon1_010505.txt", create_using=nx.DiGraph(), nodetype=int).to_undirected()
print("graph contains " + str(len(graph.nodes)) + " nodes.")

active = 0
for x in graph.nodes:
    if graph.degree[x] > 35:
        graph.nodes[x]['active'] = 1
        active += 1
    else:
        graph.nodes[x]['active'] = 0
print("top " + str(active) + " nodes marked as active.")

print(str(majority_illusion_count(graph)) + " nodes experience majority illusion.")
