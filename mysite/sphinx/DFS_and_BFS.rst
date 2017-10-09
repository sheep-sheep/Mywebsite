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