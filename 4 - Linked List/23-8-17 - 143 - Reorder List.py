
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """ 
            - The trick to this problem is to cut the list in half,
              reverse the second half, then merge the 2 lists in zipper order
            - We're just given the head, so we must traverse to the end to find 
              the length, and use length to traverse to the middle
        """
    # get middle
        # we can traverse to end and middle at the same time using 2 ptrs and moving 1 twice as much
        pMiddle = head
        pEnd = head.next
        # while pEnd is not at end
        while pEnd and pEnd.next:
            pMiddle = pMiddle.next
            # traverse the end pointer twice as fast
            pEnd = pEnd.next.next
        # some whiteboarding shows that we should start the second list at 1 after middle
    # split the list
        head2 = pMiddle.next
        pMiddle.next = None
    # reverse list 2
        # set up initial pointers
        prev = None
        cur = head2
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
        head2 = prev
    # merge the 2 lists in zipper
        # set up current ptrs for each list
        cur1 = head
        cur2 = head2
        n1 = None
        n2 = None
        # until we reach the end of the lists
        while cur1 and cur2:
            # move nexts
            n1 = cur1.next
            n2 = cur2.next
            # change pointers
            cur1.next = cur2
            cur2.next = n1
            # move curs
            cur1 = n1
            cur2 = n2


