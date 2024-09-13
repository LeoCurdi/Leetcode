
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """ 
            - We're just reversing a bunch of linked sub lists within the main list
        """
        # dummy
        dummy = ListNode(0, head)
        head1 = dummy
        # track if we're on the first cycle
        i = 0
        # infinite loop - we will exit when we reach the end of the list
        while 1:
            # update counter
            i += 1
            # get kth node
            cur = head1
            for j in range(0, k):
                # if we reached end of list before reaching kth, end function
                if not cur.next:
                    return head
                cur = cur.next
            # save head of next section of list
            head2 = cur.next
            # sever the sub list
            cur.next = None
            # reverse the sub list - we do not need to save the return value of this function becauce cur will point to the same node
            self.reverseList(head1.next)
            # if first cycle - update actual head
            if i == 1:
                head1 = cur
                head = cur
            # if not first cycle, update connection to prev sublist
            else:
                head1.next = cur
                head1 = cur
            # now traverse to the end of the reversed sublist
            while head1.next:
                head1 = head1.next
            # reconnect the sublist
            head1.next = head2


    def reverseList(self, head):
        # set up 3 ptrs
        prev, nxt = None, None
        cur = head
        # until end of list
        while cur:
            # shift next ptr
            nxt = cur.next
            # change ptrs
            cur.next = prev
            # shift prev and cur
            prev = cur
            cur = nxt
        # update head
        head = prev
        # return head
        return head

