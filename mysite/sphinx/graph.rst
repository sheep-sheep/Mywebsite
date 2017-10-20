Coding Questions - Graph
=============================

Basics
-------------

__ https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

**Graph Representation**: Here's a good `tutorial`__.

1. How long it takes to determine whether a given edge is in the graph
    * Adjacency lists
    * Edge lists

2. How long it takes to find the neighbors of a given vertex
    * Adjacency matrices

The most used or nataural way is to use *Adjacency lists*:

            .. image:: images/adjlists.png

Or we can use OOD concept to store vertex information.


**Topological Sort**: Topological Sorting for a graph is not possible if the graph is not a DAG.

An ordering of its *vertices* along a horizontal line so that all directed *edges* go from left to right.

1. Doing with DFS::
2. Doing with BFS::



LeetCode 210. Course Schedule II
-----------------------------------------

__ https://discuss.leetcode.com/topic/13873/two-ac-solution-in-java-using-bfs-and-dfs-with-explanation

My thought is clear and i construct a graph using dictionary, then i can do a BFS on this graph until number of 
courses has met. However, i failed to detect the circle and handle that case. This is really a good chance for me
to learn this kind of graph related questions.

Or saying from `website`__ this prerequisite relationship reminds one of directed graphs. Then, the problem reduces to find a topological sort order 
of the courses, which would be a DAG if it has a valid order.
