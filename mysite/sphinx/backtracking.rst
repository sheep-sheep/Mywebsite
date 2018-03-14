Coding Questions - BackTracking
=========================================
**BackTracking** is a coding pattern to solve the combination and permuation problems; Backtracking is a way to solve computational problems, wwhich incremently build candiates and abandon partial candidate(from wiki).

2018-02-04:
You don't need to treat the backtracking differently, in fact, it's just a DFS!!!??

If you have a clear way/rule to build the result set, then you already have a recusive solution, just need to handle 2 cases:
    # base case
    # the dividing case

I need a set of questions to understand the flow of this method::

        def perm(s):
            # this permutation can't handle duplicates
            if len(s)==1:
                return [s]
            res = []
            for i in range(len(s)):
                for tmp in perm(s[:i]+s[i+1:]):
                    res.append(s[i]+tmp)
            return res

        # This is a different thinking process!!!!

        def permute(self, nums):
            # permutation means at each index, you have n choices to get the number
            # and in total you have factorial of N choices
            
            # recurisve way
            def helper(tmp, choices, res):
                if not choices:
                    res.append(tmp)
                    return
                for i in range(len(choices)):
                    helper(tmp+[choices[i]], choices[:i]+choices[i+1:], res)
            if not nums:
                return []
            res = []
            helper([], nums, res)
            return res

        def combine(s):
            if len(s)==1:
                return [s]
            res = []
            for i in range(len(s)):
                res.append([s[i]])
                for tmp in combine(s[:i]+s[i+1:]):
                    res.append([s[i]]+tmp)
            return res

        def combine_1(s):
            def helper(s, k, path, res):
                if len(path) == k:
                    res.append(path)
                    return
                for i in range(len(s)):
                    helper(s[:i] + s[i + 1:], k, path + s[i], res)

            res = []
            for i in range(len(s)+1):
                helper(s, i, '', res)
            return res


        def combine_2(s):
            def helper(s, path, res):
                res.append(path)
                for i in range(len(s)):
                    helper(s[i + 1:], path + s[i], res)

            res = []
            helper(s, '', res)
            return res



LeetCode 257 Binary Tree Paths
---------------------------------------

This question is to use the DFS traversal, it's still a little different than Backtracking problems.

Recursive Solution::
        
        class Solution(object):
            def binaryTreePaths(self, root):
                res = []
                paths = []
                def dfs(root, paths, res):
                    if not root.right and not root.left:
                        paths.append(root.val)
                        res.append('->'.join(map(str, paths)))
                        return
                    if root.right:
                        dfs(root.right, paths + [root.val], res)
                    if root.left:
                        dfs(root.left, paths + [root.val], res)
                if not root:
                    return []

                dfs(root, paths, res)
                return res



The trick for stack is to save the previous result in to the stack it's obvious if you think about the recursion, it doesn't only save the function call but also the results of each call.


Iterative Solutions::

        class Solution(object):
            def binaryTreePaths(self, root):
                if not root:
                    return []
                res = []
                stack = [(root, [root.val])]

                while stack:
                    node, path = stack.pop()
                    if not node.left and not node.right:
                        res.append('->'.join(map(str,path)))
                    if node.right:
                        stack.append((node.right, path+[node.right.val]))
                    if node.left:
                        stack.append((node.left, path+[node.left.val]))

                return res


LeetCode 78. Subsets
------------------------------

Solution::

        # DFS/Recursion
        class Solution(object):
            def subsets(self, nums):
                if not nums:
                    return []
                
                # you only need go through the num once
                # build select all of them for different count
                def helper(path, choices, res):
                    res.append(path)
                    for i in range(len(choices)):
                        # add condition here to handle duplicate
                        helper(path + [choices[i]], choices[i+1:], res)
                
                nums.sort()
                res = []
                helper([], nums, res)
                return res       

        # Backtracking
            # After i checked the script, this approach is just to save space,
            # the idea is still similar to DFS solution.

            # But the idea differs a little, this one will go back to last step and get another step to check further
            # while DFS is to get all the next step and check further

            def subsets_backtracking(self, nums):
                from copy import copy
                def backtrack(res, path, nums, idx):
                    res.append(copy(path))
                    for i in range(idx, len(nums)):
                        path.append(nums[i])
                        backtrack(res, path, nums, i+1)
                        path.pop()
                res = []
                nums.sort()
                backtrack(res, [], nums, 0)
                return res         

        # Backtrack IS DFS we don't even need to use copy method

LeetCode 39. Combination Sum
-----------------------------------------

Similar idea with permutation and subset, the trick is to know the time to 
    #. terminate the recursion, for this question it's when target is smaller than 0.
    #. the way you construct the information that passes to next level will determine the final result.

Solutions::

        class Solution(object):
            def combinationSum(self, candidates, target):
                def helper(path, target, candidates, res):
                    if target == 0:
                        res.append(path)
                        return
                    if target < 0:
                        return
                    else:
                        for i in range(len(candidates)):
                            helper(path + [candidates[i]], target-candidates[i], candidates[i:], res)
                
                if not candidates:
                    return []
                
                res = []
                candidates.sort()
                helper([], target, candidates, res)
                return res



LeetCode 288. Unique Word Abbreviation
----------------------------------------
LeetCode 320. Generalized Abbreviation
----------------------------------------
LeetCode 408. Valid Word Abbreviation
----------------------------------------
LeetCode 411. Minimum Unique Word Abbreviation
------------------------------------------------