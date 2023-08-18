
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """ 
            - Double iterate through the list with a slow and fast ptr.
              If the fast ptr laps the slow ptr we have a cycle.
            - Some whiteboarding shows that if fast laps slow, there
              will for sure be a point where they're on the same node,
              as fast catches up to slow by 1 node per iteration
        """
        # set up 2 ptrs
        slow = head
        fast = head.next if head else None # short circuit in case head is null
        # go until we find the end of the list
        while fast and fast.next:
            # check if they're on the same node
            if slow == fast:
                # this means fast has lapped slow so we have a cycle - end the function here
                return True
            # shift slow ptr
            slow = slow.next
            # we dont need error handling for fast.next.next bc we covered it in the second while condition
            fast = fast.next.next
        # if we reached the end of the list - there's no cycle so return false
        return False

