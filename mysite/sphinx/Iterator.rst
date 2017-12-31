class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visit = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0 or self.visit

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