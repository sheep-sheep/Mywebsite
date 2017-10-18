Coding Questions - DFS and BFS
===================================
You have to master the most used techniques and be able to apply them on
    #. Tree

        * DFS

            * Recursive
            * Iterative

        * BFS

            * Recursive
            * Iterative

    #. Matrix

        * DFS

            * Recursive::
            
                    class Solution(object):
                        def numIslands(self, grid):
                            def helper(grid, visited, row, col, res):
                                if len(grid) > row >= 0 and len(grid[0]) > col >= 0:
                                    if not visited[row][col]:
                                        visited[row][col] = True
                                        if grid[row][col] == '1':
                                            res.append((row, col))
                                            helper(grid, visited, row + 1, col, res)
                                            helper(grid, visited, row - 1, col, res)
                                            helper(grid, visited, row, col + 1, res)
                                            helper(grid, visited, row, col - 1, res)

                            res = []
                            visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
                            for i in range(len(grid)):
                                for j in range(len(grid[0])):
                                    tmp = []
                                    helper(grid, visited, i, j, tmp)
                                    if tmp:
                                        res.append(tmp)
                            return len(res)



            * Iterative::

                    def numIslands_stack(self, grid):
                        res = []
                        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
                        for i in range(len(grid)):
                            for j in range(len(grid[0])):
                                tmp = []
                                stack = [(i, j)]
                                while stack:
                                    row, col = stack.pop()
                                    if len(grid) > row >= 0 and len(grid[0]) > col >= 0:
                                        if not visited[row][col]:
                                            visited[row][col] = True
                                            if grid[row][col] == '1':
                                                tmp.append((row, col))
                                                stack.append((row+1, col))
                                                stack.append((row-1, col))
                                                stack.append((row, col+1))
                                                stack.append((row, col-1))
                                if tmp:
                                    res.append(tmp)
                        return len(res)


        * BFS

            * Recursive

            * Iterative::

                    def numIslands_queue(self, grid):
                        res = []
                        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
                        for i in range(len(grid)):
                            for j in range(len(grid[0])):
                                queue = [(i, j)]
                                tmp = []
                                while queue:
                                    n = len(queue)
                                    while n:
                                        row, col = queue.pop(0)
                                        n -= 1
                                        if len(grid) > row >= 0 and len(grid[0]) > col >= 0:
                                            if not visited[row][col]:
                                                visited[row][col] = True
                                                if grid[row][col] == '1':
                                                    tmp.append((row, col))
                                                    queue.append((row + 1, col))
                                                    queue.append((row - 1, col))
                                                    queue.append((row, col + 1))
                                                    queue.append((row, col - 1))
                                if tmp:
                                    res.append(tmp)
                        return len(res)



    #. Graph

        * DFS

            * Recursive

            * Iterative

        * BFS

            * Recursive

            * Iterative


LeetCode 210. Course Schedule II
-----------------------------------------

__ https://discuss.leetcode.com/topic/13873/two-ac-solution-in-java-using-bfs-and-dfs-with-explanation

My thought is clear and i construct a graph using dictionary, then i can do a BFS on this graph until number of 
courses has met. However, i failed to detect the circle and handle that case. This is really a good chance for me
to learn this kind of graph related questions.

Or saying from `website`__ this prerequisite relationship reminds one of directed graphs. Then, the problem reduces to find a topological sort order 
of the courses, which would be a DAG if it has a valid order.

**Topological Sorting**: Topological Sorting for a graph is not possible if the graph is not a DAG.
    