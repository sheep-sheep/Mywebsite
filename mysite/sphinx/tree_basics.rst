Coding Questions - Tree Basics
================================

**As most binary tree problems, you want to solve this recursively.**

LeetCode 145. Binary Tree Postorder Traversal
-------------------------------------------------------------------------------

Basic Tree Operations:

    Just adjust the time to evaluate the node, each recursive method is a stack operation.
    To seperate the inorder and preorder iterative call, just print current value at different time.

    #In-Order Traversal

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


    #Pre-Order Traversal

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


    #Post-Order Traversal

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
                    stack2.append(node.val) # res.append(node.val) just use another stack to hold the results instead of printing it
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                for val in stack2:
                    res.append(val)
                return res




    #DFS

    *Recursive*
    *Iterative*

    #BFS

    *Recursive*
    *Iterative*