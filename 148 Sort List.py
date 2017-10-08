# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(head, tail, res):
            slow = head
            fast = head.next.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            res1 = sort(head, slow)
            res2 = sort(slow.next, tail)
            res_head = merge(res1, res2)
            return res_head
        
        def merge(head1, head2):
            while head1 and head2:
                if head1.val > head2.val:
                    tmp1 = head1.next
                    tmp2 = head2.next
                    head1.next = head2
                    head1.next = tmp1.next
                    head2.next = tmp2
