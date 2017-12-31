
https://leetcode.com/problems/path-sum/description/
https://leetcode.com/problems/path-sum-ii/description/
https://leetcode.com/problems/path-sum-iii/description/::

        class Solution(object):
            def pathSum(self, root, sum):
                """
                :type root: TreeNode
                :type sum: int
                :rtype: int
                """
                def dfs(root, res):
                    if not root:
                        return 0
                    return int(root.val == res) + dfs(root.left, res-root.val) + dfs(root.right, res-root.val)
                if not root:
                    return 0
                return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


https://leetcode.com/problems/path-sum-iv/description/
