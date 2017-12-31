LeetCode 337. House Robber III
==========================================

Solution 0::

    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """

            
            # my problem here is it breaks the recursion property and it won't cover all cases
            def dfs(root, robbed):
                if not root:
                    return
                if level % 2 == 0:
                    self.even += root.val
                else:
                    self.odd += root.val
                
                dfs(root.left, level+1)
                dfs(root.right, level+1)
            value1 = dfs(root, True)
            
            return max(self.even, self.odd)

Solution 1::

    class Solution(object):
        def rob(self, root):
            # my problem here is it breaks the recursion property and it won't cover all cases
            # instead of checking level, we need to check ROBBED or NOT of its parent
            
            # the standard solution is to deal with ROBBED or NOT at the same time with a [0, 1]
            def dfs(root):
                if not root:
                    return [0, 0]
                left = dfs(root.left)
                right = dfs(root.right)
                rob_curr = left[1]+right[1] + root.val
                notrob_curr = max(left[0], left[1])+max(right[0], right[1])
                return [rob_curr, notrob_curr]

            res = dfs(root)
            return max(res)