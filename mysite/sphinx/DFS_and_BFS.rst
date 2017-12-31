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
        Have a process idea which is to have 3 colors to indicate the state and mark all vertices from WHITE to GRAY and then to BLACK to indicate the search is completed.

        Always keep in mind that Graph is consisted by *Vertex* and *Edge*.

        Running time is **O(V+E)**.

        * DFS
            * Property
                * During search, we can set 2 timestemp v.d and v.f to indicate first discover and blacken the vertex.
                * **Parenthesis structure**.
                * First explore an edge (u, v):
                    + WHITE indicates a tree edge
                    + GRAY indicates a back edge
                    + BLACK indicates a forward or cross edge

            * Recursive

            * Iterative

        * BFS
            * Property
                * During search, we can set the distance between source and this vertex
            * Recursive

            * Iterative




Level Order Traversal of Binary Tree
---------------------------------------

DFS::

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        def recursive(res, root, level):
            if not root:
                return
            if level < len(res):
                res[level].append(root.val)
            else:
                res.append([root.val])
            recursive(res, root.left, level+1)
            recursive(res, root.right, level+1)
        res = []
        recursive(res, root, 0)
        return res[::-1]

    1.    TreeNode visit = root;
          Stack<TreeNode> stack = new Stack();
    2.    while (visit != null || !stack.empty()) {
    3.        while (visit != null) {
                  stack.push(visit);
                  visit = visit.left;
              }
              TreeNode next = stack.pop();
              visit = next.right;
              doSomethingWith(next.val);
          }

BFS::
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        final = []
        queue = []
        queue.append(root)
        while queue:
            res = []
            # we have queue and we need to get each level
            # this is done by get the size of queue which is the size of the level
            n = len(queue)
            while(n):
                node = queue.pop(0)    
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            final.append(res)
        return final[::-1]