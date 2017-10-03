Coding Questions - Linked List
=========================================

**Two Pointers**, this is a very useful trick to deal with linked list problems.

LeetCode 109. Convert Sorted List to Binary Search Tree
----------------------------------------------------------

This is using the 2 pointers to operate the linked list::
        class Solution(object):
            def sortedListToBST(self, head):

                import copy
                if not head:
                    return None
                def helper(head, tail):
                    slow = copy.copy(head)
                    fast = copy.copy(head)
                    if head==tail:
                        return None
                    while(fast != tail and fast.next != tail):
                        fast = fast.next.next
                        slow = slow.next
                    midroot = TreeNode(slow.val)
                    midroot.left = helper(head, slow)
                    midroot.right = helper(slow.next, tail)
                    return midroot
                
                return helper(head, None)