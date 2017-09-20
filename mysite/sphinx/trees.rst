Coding Questions - Trees
===========================
This page will collect all the **Tree** related questions.

**As most binary tree problems, you want to solve this recursively.**

LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
-------------------------------------------------------------------------------

This is my observation of the 2 array::
    All elements left of root must be in the left subtree and all elements to the right must be in the right subtree.

Source Code::
    class Solution(object):
        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            def helper(preIdx, inStart, inEnd, preorder, inorder):
                if preIdx > len(preorder)-1 or inStart > inEnd:
                    return None
                
                root = TreeNode(preorder[preIdx])
                inIdx = inorder.index(preorder[preIdx])
                root.left = helper(preIdx+1, inStart, inIdx-1, preorder, inorder)
                root.right = helper(preIdx+inIdx-inStart+1, inIdx+1, inEnd, preorder, inorder)
                return root
            
            return helper(0, 0, len(inorder) - 1, preorder, inorder)





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

