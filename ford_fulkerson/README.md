# Ford-Fulkerson Algorithm

In the following exrecises we use a graph to model a network flow(e.g., traffic flow, liquid flow, electric current flow etc.). To do this we consider   a directed (a flow has some direction), weighted (particular segments of a network have some capacities) graph G=(V,E,c), where c stands for a capacity matrix such that for each pair of graph vertices (u,v)∈V×V a capacity (maximum flow) between uand v, c(u,w), is given (in other words, a maximum transfer allowed for a given "channel").  If u and v are not connected  or transfer from  uto v is not possible then c(u,v)=0. We distinguish two graph vertices s,t∈V which denote the network flow source and target (also referred to as a sink) respectively.

Now we ask the question: what is the maximum flow possible between a source (s) and a target (t). For water flow, for instance, it may be asked: how much liters of water can be pumped between s and t in one second? To answer this one has to launch the Ford-Fulkerson algorithm which pseudocode is given below.

## Exercise 1 

Implement the following F-F algorithm pseudocode

### FFA INPUT

```
G=(V,E,c) - network graph

c:V×V→R - network capacity matrix

s - source vertex

t - target vertex
```

### FFA OUTPUT

```
f:V×V→R - flow matrix
```

Remark: The graph Gf=(V,Ef,cf) used below is called a residual network, i.e., a graph such that  ∀(u,v)∈V×V:cf(u,v)=c(u,v)−f(u,v)>0. Gf contains all vertices of G and those edges of G for which a maximum flow has not been reached so far. The algorithm's performance is aimed at increasing flows f in G up to the moment when there is no path from s to t in a residual graph, i.e., no further flow growth is possible.

```
Ford–Fulkerson(G=(V,E,c),s,t)
f(u,v) \leftarrow 0 for all edges (u,v)
while exists a path  p from s to t in the graph Gf , such that cf(u,v)>0 for all edges belonging to p:
Find c_f(p) = \min\{c_f(u,v) : (u,v) \in p\}
For each (u,v) \in p
f(u,v) \leftarrow f(u,v) + c_f(p)
f(v,u) \leftarrow f(v,u) - c_f(p)
```

## Exercise 2

Calculate maximum flow between vertices 10 and  60 of the [test graph](https://github.com/sowmya6598/algorithms-data-structures/blob/master/ford_fulkerson/graf1.txt)

## Exercise 3

For the same [test graph](https://github.com/sowmya6598/algorithms-data-structures/blob/master/ford_fulkerson/graf1.txt) find a target vertex  for which the maximum flow from the source s=10 is reached.
