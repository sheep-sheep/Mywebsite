Coding Questions - Tree Basics
================================

**As most binary tree problems, you want to solve this recursively.**

LeetCode 145. Binary Tree Postorder Traversal
-------------------------------------------------------------------------------

Basic Tree Operations:

    Just adjust the time to evaluate the node, each recursive method is a stack operation.
    To seperate the inorder and preorder iterative call, just print current value at different time.

    #. In-Order Traversal

        *Recursive*::

            def inorder_recurr(root, res):
                if root:
                    traverse_recurr(root.left, res)
                    res.append(root.val)
                    traverse_recurr(root.right, res)
                    return res


        *Iterative*::

            def inorder_iterative(root, res):
                res = []
                stack = []
                while True:
                    while root:
                        stack.append(root)
                        root = root.left
                    if not stack:
                        return stack
                    node = stack.pop()
                    res.append(node.val)
                    root = node.right
                return res


    #. Pre-Order Traversal

        *Recursive*::

            def inorder_recurr(root, res):
                if root:
                    res.append(root.val)
                    traverse_recurr(root.left, res)
                    traverse_recurr(root.right, res)
                    return res


        *Iterative*::

            def preorder_traverse_stack_0(root):
                stack = []
                res = []
                stack.append(root)
                while(stack):
                    node = stack.pop()
                    res.append(node.val)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                return res

            def inorder_iterative_1(root, res):
                res = []
                stack = []
                while True:
                    while root:
                        res.append(node.val)
                        stack.append(root)
                        root = root.left
                    if not stack:
                        return stack
                    node = stack.pop()
                    root = node.right
                return res


    #. Post-Order Traversal

    According to oberservation, the post order is just the preorder, put the root after child tree.
    Another interpretation is the print node method is called after stack call.

        *Recursive*::

            def inorder_recurr(root, res):
                if root:
                    res.append(root.val)
                    traverse_recurr(root.left, res)
                    traverse_recurr(root.right, res)
                    return res
        


        *Iterative*::

            def postorder_traverse_stack(root):
                stack = []
                stack2 = []
                res = []
                stack.append(root)
                while stack:
                    node = stack.pop()
                    stack2.append(node.val)  # res.append(node.val) just use another stack to hold the results instead of printing it
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                for val in stack2[::-1]:
                    res.append(val)
                return res

            def postorder_traverse_stack(root):
                stack = []
                res = []
                while True:
                    while root:
                        if root.right:
                            stack.append(root.right)
                        stack.append(root)
                        root = root.left
                    if not stack:
                        return res
                    root = stack.pop()
                    if root.right and stack and stack[-1] == root.right:
                        stack.pop()
                        stack.append(root)
                        root = root.right
                    else:
                        res.append(root.val)
                        root = None
                return res


    #. BFS

        *Recursive*::
            # If you want to use recursive, you have to find the right varaible to pass between
            # different values

            # the list that passes between levels are final list
            # find the statement to update that final list
            def recursive(res, root, level):
                if not root:
                    return
                if level < len(res):
                    res[level].append(root.val)
                else:
                    res.append([root.val])
                recursive(res, root.left, level+1)
                recursive(res, root.right, level+1)


        *Iterative*：：
            def BFS(self, root):
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
                return final


    #. Morris Traversal
        ?????


class Codec_0:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node != None:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return '['+ ', '.join(res)+']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('[]{}').split(',')
        if not data:
            return None
        root = TreeNode(data[0])
        queue = [root]
        i = 0
        while i < len(data) and queue:
            node = queue.pop(0)
            if i + 1 < len(data) and data[i+1] != 'None':
                node.left = TreeNode(data[i+1])
                queue.append(node.left)
            if i + 2 < len(data) and data[i + 2] != 'None':
                node.right = TreeNode(data[i+2])
                queue.append(node.right)
            i += 2
        return root


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        stack = [root]
        res = []

        while stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left

            res.append('None')
            node = stack.pop()
            if not node:
                res.append('None')
            else:
                root = node.right

        return '['+ ', '.join(res)+']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('[]{}').split(',')
        if not data:
            return None
        root = TreeNode(data[0])
        stack = [root]
        x= stack[-1]
        i = 1
        while i < len(data):
            while i < len(data) and data[i] != 'None':
                root.left = TreeNode(data[i])
                root = root.left
                stack.append(root)
                i += 1
            while i < len(data) and data[i] == 'None' and stack:
                root = stack.pop()
                i += 1
            if i < len(data):
                root.right = TreeNode(data[i])
                root = root.right
                stack.append(root)
                i += 1
        return x        