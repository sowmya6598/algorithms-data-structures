import networkx as nx
import math
from collections import defaultdict
import scipy
from scipy import sparse

graph1 = nx.DiGraph()     # To drow the graph:

graph1 = nx.read_edgelist(r"C:\Users\sthottam\PycharmProjects\fordfulkerson\graf1.txt", delimiter="\t",
                         create_using = nx.DiGraph(), nodetype=int, data=(('capacity', float), ))

for i in graph1.edges():           #To genurate and print the founded cycles
    graph1[i[0]][i[1]]['flow'] = 0.00
    adjacency = [(n, nbrdict) for n, nbrdict in graph1.adjacency ()]
#print("cycles found :")
#print(nx.find_cycle(graph1))
X = nx.adj_matrix(graph1)
X = X.todense()
adjacencySparse = X


def ford_fulkerson(graph, source, sink, debug=None):          # To implement ford fulkerson algorithm:
    graph1 = nx.graph.deepcopy(graph)
    flow, path = 0, True
    graph2 = nx.to_dict_of_dicts(graph1)
    path = nx.shortest_path(graph1, source, sink)
    while path:               # searching for the path with the flow reserve
        reserve = float(math.inf)
        #print(path)
        for x in range(0,len(path)-1):
            rate = graph1[path[x]][path[x+1]]['capacity']
            if (rate < reserve):
                reserve = graph1[path[x]][path[x+1]]['capacity']
        flow += reserve
        for x in range(0, len(path) - 1):
            graph1[path[x]][path[x + 1]]['capacity'] -= reserve
            graph1[path[x]][path[x + 1]]['flow'] += reserve

        for x in range(0, len(path) - 1):           #The removed vertices
            if(graph1[path[x]][path[x + 1]]['capacity']) <=0:
                #print("Deleted :",path[x], path[x+1])
                graph1.remove_edge(path[x], path[x+1])

        for v, u in zip(path, path[1:]):                     # Increasing the flow along the path
            if graph1.has_edge(v, u):
                graph1[v][u]['flow'] += reserve
            else:
                if( graph1.has_edge(u,v)):
                    graph1[u][v]['flow'] -= reserve

        try:
            path = nx.shortest_path(graph1,source,sink)
        except:
            path = None

        if callable(debug):                         # showing interpose results
            debug(graph1, path, reserve, flow)
    return flow


def depth_first_search(J, source, sink):
    not_directed = J.to_undirected()
    not_directed = nx.to_dict_of_dicts(not_directed)
    scout = {source}
    heap = [(source, 0, not_directed[source])]

    while heap:                 #searching neighbors
        v, _, neighbours = heap[-1]
        if v == sink:
            break

        while neighbours:         #function searching the next neighbor
            u, e = neighbours.popitem()
            if u not in scout:
                break
        else:
            heap.pop()
            continue

        in_direction = G.has_edge(v, u)     #The capacity
        capacity = e['capacity']
        flow = e['flow']

        if in_direction and flow < capacity:    #to make the flow from edges increasing
            heap.append((u, capacity - flow, not_directed[u]))
            scout.add(u)
        elif not in_direction and flow:
            heap.append((u, flow, not_directed[u]))
            scout.add(u)

    reserve = min((f for _, f, _ in stack[1:]), default=0)
    path = [v for v, _, _ in stack]

    return path, reserve


f = ford_fulkerson(graph1, 10, 60)
print("from 10 to 60")
print(f)

mmax = -1
xx = None
for x in graph1.nodes():
        y =  ford_fulkerson(graph1, 10,x )
        if (mmax < y):
            xx = x
            print(y, "  ", xx)
        mmax = max(y,mmax)

print(mmax, "  ",xx)

