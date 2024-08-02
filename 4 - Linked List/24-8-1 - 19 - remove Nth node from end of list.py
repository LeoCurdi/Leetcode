# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - given: head of singly linked list
        - find: function to remove Nth node from the end

        - use 2 pointers, one is N nodes ahead of the other
        - when the right pointer reaches the end, remove the node at the left pointer
        """
        # create a dummy node before the head (always nice for edge cases)
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # put N nodes between left and right
        i = 1
        while i < n:
            right = right.next 
            i += 1

        # traverse to end of list
        while right.next:
            right = right.next
            left = left.next

        # remove the node to the right of the left pointer
        left.next = left.next.next
        
        return dummy.next

