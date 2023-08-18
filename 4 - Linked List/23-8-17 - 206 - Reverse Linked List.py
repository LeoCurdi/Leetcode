
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """ 
            - To reverse a singly linked list:
              - point prev to null, cur to head, and next to cur->next
              - iterate until cur = null, pointing cur.next to prev
                and shifting prev, cur, and next
              - then point head to end (prev)
        """
        # set up initial pointers
        prev = None # None is python for null
        cur = head
        n = None
        # iterate until cur is null
        while cur:
            # shift next ptr
            n = cur.next
            # point cur to prev
            cur.next = prev
            # shift prev and cur
            prev = cur
            cur = n
        # point head to end
        head = prev
        # we have to return head lol
        return head





