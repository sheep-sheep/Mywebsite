Segment Tree (Range Sum)
=======================================
1.  Query:  O(n)
    Update: O(1)

2.  Query:   O(1)
    Update:  O(n)

3.  Query:   O(logn)
    Update:  O(logn)


Implementation of SegmentTree::

        class Node(object):
            def __init__(self, val, start, end):
                self.val = val
                self.start = start
                self.end = end
                self.left = None
                self.right = None


        class NumArray(object):
            def __init__(self, nums):
                """
                :type nums: List[int]
                """
                self.root = self.build(0, len(nums)-1, nums)

            def build(self, start, end, nums):
                if start > end:
                    return None
                if start == end:
                    return Node(nums[start], start, end)
                mid = (start + end)/2
                left = self.build(start, mid, nums)
                right = self.build(mid+1, end, nums)
                node = Node(left.val+right.val, start, end)
                node.left = left
                node.right = right
                return node

            def query(self, root, start, end):
                if start > root.end or end < root.start:
                    return 0
                if root.start == start and root.end == end:
                    return root.val
                mid = (root.start + root.end)/2

                if start <= mid:
                    if end <= mid:
                        return self.query(root.left, start, end)
                    else:
                        return self.query(root.left, start, mid) + self.query(root.right, mid+1, end)
                else:
                    return self.query(root.right, start, end)

            def modify(self, root, index, val):
                if root.start == root.end == index:
                    root.val = val
                    return
                mid = (root.start + root.end)/2
                if index <= mid:
                    self.modify(root.left, index, val)
                else:
                    self.modify(root.right, index, val)

                root.val = root.left.val + root.right.val
                return


Implementation of Binary Indexed Tree::

        class BIT(object):

            def __init__(self, nums):
                self.nums = [0]*(len(nums)+1)
                for i in range(len(nums)):
                    self.update(i+1, nums[i])


            def update(self, idx, val):
                while idx < len(self.nums):
                    self.nums[idx] += val
                    idx += idx&(-idx)


            def querySum(self, idx):
                res = 0
                while idx > 0:
                    res += self.nums[idx]
                    idx -= idx&(-idx)
                return res                