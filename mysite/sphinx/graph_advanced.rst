Advanced Graph Algorithm
===================================

Minimum Spanning Tree
---------------------------

Properites:
    # It's a tree which means there's no cycle
    # It's based on non-directed graph


How to find a spanning tree?
    Core idea is to use greedy algorithm and for each step find the edge with minimum weight.


Two ways to build:
    # Kruskal's algorithm:
        Sort the edge based on weight, then adding each edge to the tree without forming a 
        cycle.

    # Prim's algorithm
        Starting from any vertex, insert the adjacent vertices into PQ, and choose the vertex
        with minimum edge weight

Data Structure:
    Priority Queue
    Union Find

Dijkstra's algorithm
-------------------------------------------------------

Single Source Shortest Path
Dijkstra's algorithm initializing dist[s] to 0 and all other distTo[] entries to positive infinity. Then, it repeatedly relaxes and adds to the tree a non-tree vertex with the lowest distTo[] value, continuing until all vertices are on the tree or no non-tree vertex has a finite distTo[] value.

Data Structures:
    
    . Priority Queue
    . Edges on the shortest-paths tree: edgeTo[v] is the the last edge on a shortest path from s to v.
    . Distance to the source: distTo[v] is the length of the shortest path from s to v.



Edge_weighted DAG

Negative Cycles:

Bellman-Ford algorithm. 

Initialize distTo[s] to 0 and all other distTo[] values to infinity. Then, considering the digraph's edges in any order, and relax all edges. Make V such passes::

        for (int pass = 0; pass < G.V(); pass++)
           for (int v = 0; v < G.V(); v++)
              for (DirectedEdge e : G.adj(v))
                  relax(e);

Arbitrage detection. Consider a market for financial transactions that is based on trading commodities.
