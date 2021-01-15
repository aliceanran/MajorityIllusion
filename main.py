import networkx as nx

graph = nx.read_edgelist("oregon1_010505.txt", create_using=nx.DiGraph(), nodetype=int).to_undirected()
print("graph contains " + str(len(graph.nodes)) + " nodes.")

# graph_by_node_degree = sorted(graph.degree, key=lambda x: x[1], reverse=True)
# print(graph_by_node_degree)
# print(graph_by_node_degree[104])

active = 0
for x in graph.nodes:
    if graph.degree[x] > 35:
        graph.nodes[x]['active'] = 1
        active += 1
    else:
        graph.nodes[x]['active'] = 0
print("top " + str(active) + " nodes marked as active.")

illusion = 0
for x in graph.nodes:
    active_neighbors = 0
    for n in graph.adj[x]:
        if graph.nodes[n]['active'] == 1:
            active_neighbors += 1
    if active_neighbors / len(graph.adj[x]) >= 0.5:
        illusion += 1

print(str(illusion) + " nodes experience majority illusion.")