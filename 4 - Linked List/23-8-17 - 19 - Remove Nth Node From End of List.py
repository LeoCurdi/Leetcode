
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """ 
            - Make 2 pointers. Point 1 to head and 1 n nodes ahead of head
            - Then traverse both until the end one reaches end
            - Delete the node between the 2 pointers
            - Since we're using a 2 pointer approach time is o(N)
        """
        # set up ptrs
        prev = head
        end = head
        # move next ptr until it is n nodes ahead of head
        for i in range(n):
            end = end.next
        # traverse both ptrs until end reaches end
        while end and end.next:
            prev = prev.next
            end = end.next
        # now prev pts to n-1 from end so we must delete prev.next
        # edge case: we're deleting first node - p still pts to head and e is null
        if prev == head and end == None:
            # point head to the next node
            if prev.next:
                head = prev.next
            else:
                head = None
            # return here so we skip the rest of the function
            return head
        # grab the target node in a temp
        deletedNode = prev.next
        # connect prev to next.next
        prev.next = prev.next.next
        # remove deleted node's connection
        deletedNode.next = None
        # return the head (we could also return the deleted node but that's not what they're asking)
        return head



