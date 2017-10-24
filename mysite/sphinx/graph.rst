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

1. Doing with DFS:
2. Doing with BFS:



LeetCode 207. Course Schedule
-----------------------------------------

__ https://discuss.leetcode.com/topic/13873/two-ac-solution-in-java-using-bfs-and-dfs-with-explanation

My thought is clear and i construct a graph using dictionary, then i can do a BFS on this graph until number of 
courses has met. However, i failed to detect the circle and handle that case. This is really a good chance for me
to learn this kind of graph related questions.

Or saying from `website`__ this prerequisite relationship reminds one of directed graphs. Then, the problem reduces to find a topological sort order 
of the courses, which would be a DAG if it has a valid order.

This problem can be solved in 3 different ways:
#. Detecting a cycle BFS/DFS.
#. Using topological sort
#. Union-Find?


If you treat it as a cycle detection problem, you can use a graph traversal method and detect a cycle along the traverse.
Thus there're 2 versions of cycle detection.

DFS::
        
        # Adjacency List solution to detect cycle
        class Solution(object):
            def canFinish(self, numCourses, prerequisites):
                """
                :type numCourses: int
                :type prerequisites: List[List[int]]
                :rtype: bool
                """
                from collections import defaultdict
                graph = defaultdict(list)
                # initilize the graph
                # since the question is assuming we will have n courses in total which makes
                # initializing the graph much easier.
                def buildGraph(graph, numCourses, edgelists):
                    for i in range(numCourses):
                        graph[i]
                    for edge in edgelists:
                        graph[edge[0]].append(edge[1])
                    return graph
                
                graph = buildGraph(graph, numCourses, prerequisites)
                WHITE = 1
                BLACK = 2
                GREY = 3
                self.visited = [WHITE for _ in range(numCourses)]
                self.circle = 0
                
                def DFS_Visit(graph, vertex):
                    self.visited[vertex] = GREY
                    for adj_vertex in graph[vertex]:
                        if self.visited[adj_vertex] == WHITE:
                            DFS_Visit(graph, adj_vertex)
                        elif self.visited[adj_vertex] == GREY:
                            self.circle += 1
                    self.visited[vertex] = BLACK
                
                for vertex in range(numCourses):
                    if self.visited[vertex] == WHITE:
                        DFS_Visit(graph, vertex)
                
                return self.circle == 0


BFS::

        class Solution(object):
            def canFinish(self, numCourses, prerequisites):
                """
                :type numCourses: int
                :type prerequisites: List[List[int]]
                :rtype: bool
                """
                from collections import defaultdict
                graph = defaultdict(list)
                def buildGraph(graph, numCourses, edgelists):
                    for i in range(numCourses):
                        graph[i]
                    for edge in edgelists:
                        graph[edge[0]].append(edge[1])
                    return graph
                graph = buildGraph(graph, numCourses, prerequisites)
                WHITE = 1
                BLACK = 2
                GREY = 3
                visited = [WHITE for _ in range(numCourses)]
                circle = 0
                
                queue = [0]
                visited[0] = GREY
                while queue:
                    vertex = queue.pop(0)
                    for adj_vertex in graph[vertex]:
                        if visited[adj_vertex] == WHITE:
                            visited[adj_vertex] = GREY
                            queue.append(adj_vertex)
                        elif self.visited[adj_vertex] == GREY:
                            circle += 1
                    visited[vertex] = BLACK
                return circle == 0


