Coding Questions - Binary Serach Tree
=========================================

LeetCode 297. Serialize and Deserialize Binary Tree
--------------------------------------------------------------

I will use this question to practise all Binary Tree related questions, and i can practice the possible way to
construct a Binary Tree.

In fact, it'related, if you can pass 2 orders of traversal, then you can definitely recover the tree without knowing
any other properties!


LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
-------------------------------------------------------------------------------

This is my observation of the 2 array:
    All elements left of root must be in the left subtree and all elements to the right must be in the right subtree.

Source Code::

        class Solution(object):
            def buildTree(self, preorder, inorder):
                # Trick is after we get left node, we will move preorder's pointer by number of nodes in left tree
                
                def helper(rootIdx, inStart, inEnd, preOrder, inOrder):
                    if inStart > inEnd or rootIdx > len(preOrder)-1:
                        return None
                    root = TreeNode(preOrder[rootIdx])
                    rootInxInOrder = inOrder.index(preOrder[rootIdx])
                    # rootIdx+1, the next one after root in preOrder will be left tree's root
                    # inStart, the first part of inOrder array will be the left tree's begining
                    # rootInxInOrder-1, the ending bound of left tree
                    root.left = helper(rootIdx+1, inStart, rootInxInOrder-1, preOrder, inOrder)
                    # rootIdx+1 + rootInxInOrder-inStart, the next one + size of left tree = right tree's root in preOrder
                    # rootInxInOrder+1, the second part of inOrder array will be the right tree's begining
                    # inEnd, the ending bound of right tree
                    root.right = helper(rootIdx+1+rootInxInOrder-inStart, rootInxInOrder+1, inEnd, preOrder, inOrder)
                    return root
                
                return helper(0, 0, len(preorder)-1, preorder, inorder))

        class Solution(object):
            def buildTree(self, inorder, postorder):
                """
                :type inorder: List[int]
                :type postorder: List[int]
                :rtype: TreeNode
                """
                def helper(rootIdx, inStart, inEnd, inorder, postorder):
                    if rootIdx<0 or inStart>inEnd:
                        return None
                    root = TreeNode(postorder[rootIdx])
                    rootIdxInorder = inorder.index(postorder[rootIdx])
                    root.right = helper(rootIdx-1, rootIdxInorder+1, inEnd, inorder, postorder)
                    root.left = helper(rootIdx-1-(inEnd-rootIdxInorder), inStart, rootIdxInorder-1, inorder, postorder)
                return helper(len(postorder)-1, 0, len(postorder)-1, inorder, postorder)



Follow up: How do you solve it in iterative way?!!??


LeetCode 109. Convert Sorted List to Binary Search Tree
-------------------------------------------------------------------------------
This problem we can have 2 approaches:
    #. Build the tree directly
    #. Build a tree and then make it height balanced

Forget about the 2nd solution, just using linked list, we need to find the middle of linked list.

Using 2 pointers, **SPEED** is different::

        class Solution(object):
            def sortedListToBST(self, head):
                if not head:
                    return 
                if not head.next:
                    return TreeNode(head.val)
                # here we get the middle point,
                # even case, like '1234', slow points to '2',
                # '3' is root, '12' belongs to left, '4' is right
                # odd case, like '12345', slow points to '2', '12'
                # belongs to left, '3' is root, '45' belongs to right
                slow, fast = head, head.next.next
                while fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
                # tmp points to root
                tmp = slow.next
                # cut down the left child
                slow.next = None
                root = TreeNode(tmp.val)
                root.left = self.sortedListToBST(head)
                root.right = self.sortedListToBST(tmp.next)
                return root




**What is Height Balanced BST?**
With the BST property, if you keep inserting ascending numbers to the tree, it's probably a leaned tree with no branches which
will make all the search hit work case.
This can be avoid by using a method called *height balancing*, sometimes called *AVL trees*.

**Height**
Height of a leaf:       1
Height of a tree:       root's height
Height of a empty tree: 0


**Height-balancing requirement**
A node in a tree is height-balanced if the heights of its subtrees differ by no more than 1. 
(That is, if the subtrees have heights h1 and h2, then | h1 − h2 | ≤ 1.) A tree is height-balanced if all of its nodes are height-balanced. (An empty tree is height-balanced by definition.)

**Rotation**
    #. zig-zig: single rotation
    #. zig-zag: double rotation(just call a single-rotation function twice)
    #. insert a new node and then check from bottom to root to make sure each sub-tree meets the requirement

**AVL trees**
Trees which remain balanced - and thus guarantee O(logn) search times - in a dynamic environment. Or more importantly, since any tree can be re-balanced - but at considerable cost - can be re-balanced in O(logn) time.    


LeetCode 113. Path Sum II
---------------------------------------

The core idea of this problem is to print out all root-to-leaf path during the traversal::

        final = []
        def paths(root, res):
            if root:
                if not root.left and not root.right:  # this is the leaf node
                    final.append(res + [root.val])
                else:
                    # here we have to create 2 different lists
                    # res.append(root.val)
                    paths(root.left, res+[root.val])
                    paths(root.right, res+[root.val])


Or we can remove the global variable and pass it along the call::

        def paths_dfs(root, tmp, res):
            if not root.left and not root.right:
                res.append(tmp + [root.val])
            if root.left:
                paths_dfs(root.left, tmp+[root.val], res)
            if root.right:
                paths_dfs(root.right, tmp+[root.val], res)

After we have the recursive solution, convert it to Iterative using stack::

        # since stack only can record the level, we need one more stack to get the paths
        def paths_stack(root):
            stack = [(root, [root.val])]
            res = []
            while stack:
                node, tmp = stack.pop()
                if not node.left and not node.right:
                    res.append(tmp)
                if node.left:
                    stack.append((node.left, tmp + [node.left.val]))
                if node.right:
                    stack.append((node.right, tmp + [node.right.val]))
            return res

And you have to know how to solve it using Queue::

        def paths_queue(root):
            queue = [(root, [root.val])]
            res = []
            while queue:
                n = len(queue)
                while n:
                    node, tmp = queue.pop(0)
                    n -= 1
                    if not node.left and not node.right:
                        res.append(tmp)
                    if node.left:
                        queue.append((node.left, tmp+[node.left.val]))
                    if node.right:
                        queue.append((node.right, tmp + [node.right.val]))
            return res



LeetCode 208. Implement Trie (Prefix Tree)
----------------------------------------------

Improvements:
#. Add a common search function to reduce the code
#. Think about how to do delete and print all methods


Add the method to do delete and we also need a method to print all possible words, this
is a really good exercise for the Tree-Node structure::

    class TrieNode(object):
         def __init__(self, key=None):
            self.key = key # means it's empty
            self.leaf = False # means it's a leaf
            self.children = dict()
        
    class Trie(object):

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root = TrieNode()

        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            current = self.root # the root is always empty
            for c in word:
                if c in current.children:
                    current = current.children[c]
                else:
                    current.children[c] = TrieNode(c)
                    current = current.children[c]
            current.leaf = True # this is the end      
            

        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            current = self.root
            for c in word:
                if c not in current.children:
                    return False
                else:
                    current = current.children[c]
            return current.leaf # if it's a leaf means we have save all word in Trie
            

        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            current = self.root
            for c in prefix:
                if c not in current.children:
                    return False
                current = current.children[c]
            return True


    [Ref] https://www.cs.bu.edu/teaching/c/tree/trie/
    [Ref] https://leetcode.com/problems/implement-trie-prefix-tree/discuss/


LeetCode 110. Balanced Binary Tree
----------------------------------------------

This question uses the basic recusive way to find height, the additional part is
to find a way to check **every** node is balanced instead of only checking root.left and root.right::

    # Recursive way
    class Solution(object):
        def isBalanced(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            def height(root):
                if root is None:
                    return 0
                left = height(root.left)
                right = height(root.right)
                # this additional logic will pass the flag all the way to the root
                if abs(left-right)>1 or left==-1 or right==-1:
                    return -1
                return max(left, right)+1
            return height(root)!=-1    



We have 2 Iterative ways to do the traversal:
    #. Using Stack do DFS
    #. Using Queue do BFS

::

    # InOrder Traverse Stack
    def traverse_stack(root):
        stack = []
        res = []
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res


    # BFS with Queue
    def bfs(root):
        from Queue import Queue
        q = Queue()
        res, final= [],[]
        q.put(root)
        while(not q.empty()):
            n = q.qsize()
            while n:
                node = q.get()
                res.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                n -= 1
            print res
            final.append(res)
            res=[]
        return final


    # Iterator class
    class BSTIterator(object):
        def __init__(self, root):
            """
            :type root: TreeNode
            """
            self.visit = root
            self.stack = [root]

        def hasNext(self):
            """
            :rtype: bool
            """
            return len(self.stack) != 0

        def next(self):
            """
            :rtype: int
            """
            while self.visit:
                self.stack.append(self.visit)
                self.visit = self.visit.left
            node = self.stack.pop()
            self.visit = node.right
            return node.val

        if __name__ == '__main__':
            from bst import tree

            root = tree()
            i, v = BSTIterator(root), []
            while i.hasNext():
                v.append(i.next())
            print v


LeetCode 108. Convert Sorted Array to Binary Search Tree
------------------------------------------------------------

This concept is about **Balanced BST**
If you want the tree to be balanced, then always choose the mid value as the root::

        class Solution(object):
            def sortedArrayToBST(self, nums):
                """
                :type nums: List[int]
                :rtype: TreeNode
                """
                def helper(nums, lo, hi):
                    if lo > hi:
                        return None
                    mid = lo + (hi-lo)/2
                    node = TreeNode(nums[mid])
                    node.left = helper(nums, lo, mid-1)
                    node.right = helper(nums, mid+1, hi)
                    return node
                return helper(nums, 0, len(nums)-1)
                
