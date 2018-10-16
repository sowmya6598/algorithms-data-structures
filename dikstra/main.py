import networkx as nx
import matplotlib.pyplot as plt
import math
import pylab

graph = nx.Graph()
graph = nx.read_edgelist(r"C:\Users\sthottam\Documents\GitHub\algorithms-data-structures\dikstra\graf.txt", delimiter=";",
                         create_using=nx.DiGraph(), nodetype=int, data=(('weight', float),))
edges = graph.edges()
nodes = graph.nodes()
node_edges = graph.edges([1])
weight12 = graph[1][2]["weight"]
neighbors = graph[1]


def dijkstra(g, source):
    q = []
    dist = {}
    prev = {}

    for v in g:
        dist[v] = float('inf')
        prev[v] = None
        q.append(v)

    dist[source] = 0.0

    minimum_vertex = -1
    while len(q) > 0:
        minimum = float(math.inf)
        for vertex in q:
            if dist[vertex] < minimum:
                minimum = dist[vertex]
                minimum_vertex = vertex
        q.remove(minimum_vertex)

        for v in g[minimum_vertex]:
            alt = dist[minimum_vertex] + g[minimum_vertex][v]["weight"]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = minimum_vertex
    return dist, prev


def find_shortest_path(prev, start, finish):
    sequence = []
    u = finish
    if u == start or u in prev.keys():
        while u is not None:
            sequence.append(u)
            u = prev[u]
    sequence = list(reversed(sequence))
    return sequence


distance, previous = dijkstra(graph, 1)
print("distance", distance)
print("previous", previous)
road = find_shortest_path(previous, 1, 20)
print(road)
print("comparison with inbuilt function dijkstra_path")
test_path = nx.dijkstra_path(graph, 1, 20)
print("comparison path", test_path)


fig = plt.figure(tight_layout=False)
for e in graph.edges():
    graph[e[0]][e[1]]['color'] = 'green'
    graph[e[0]][e[1]]['width'] = 1.5

for i in range(0,len(road)-1):
    graph[road[i]][road[i+1]]['color'] = 'blue'
    graph[road[i]][road[i+1]]['width'] = 5.0


pos = nx.spring_layout(graph)
edge_labels=dict([((u, v,), d['weight']) for u,v,d in graph.edges(data=True)])
edge_color_list = [graph[e[0]][e[1]]['color'] for e in graph.edges()]
widths = [graph[u][v]["width"] for u, v in edges]
nx.draw(graph, pos, edges=edges, edge_color=edge_color_list, with_labels=True, font_weight='bold', width=widths)

edges2 = []
nodes2 = []
weights2 = []
graph2 = nx.DiGraph()
for i in range(0,len(road)-1):
    graph2.add_edge(road[i], road[i+1], weight = graph[road[i]][road[i+1]]['weight'])
    graph2.add_node(road[i])
    if i == len(road)-1:
        graph2.add_node(road[i+1])
    graph2[road[i]][road[i+1]]['width'] = 5.0
    graph2[road[i]][road[i+1]]['color'] = 'blue'
pos2 = nx.spring_layout(graph2)
labels2 = nx.get_edge_attributes(graph2, 'weight')
edge_color_list2 = [graph2[e[0]][e[1]]['color'] for e in graph2.edges()]
widths = [graph2[u][v]["width"] for u,v in graph2.edges()]
nx.draw(graph2, pos, edge_color = edge_color_list2, with_labels=True, font_weight='bold', width=widths, weight=weights2)
nx.draw_networkx_edge_labels(graph2,pos,edge_labels=labels2)

print(distance[20])

