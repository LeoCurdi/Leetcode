
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """ 
            - Singly linked lists and we are given head of each
            - This is basically the merge part of merge sort
            - make a new list, compare a value from each list, insert 
              the lesser one into the new list, repeat until 1 list is 
              empty, then append the nonempty list to the result list
            - We could merge list2 into list 1 but there are so many 
              edge cases that it's not even worth it
        """
        # set up a new list by making a node to serve as head
        # Note: we wont be filling this list with a bunch of new nodes,
        # we will just edit ptrs to incorporate the nodes we already have
        # into a newly ordered list.
        # Then we will return newList.next as that will be the first actual node
        newList = ListNode()
        # set up a current pointer for the new list
        curNew = newList
        # set up cur ptrs for the 2 input lists
        cur1 = list1
        cur2 = list2
        # go until we get to the end of one of the lists
        while cur1 and cur2:
            # compare the 2 values, insert the smaller one into the new list
            # update ptrs
            if cur1.val < cur2.val:
                # insert - just update ptr (we dont need to make new nodes)
                curNew.next = cur1
                # update cur1
                cur1 = cur1.next
            # else (values are equal or v2 is less)
            else:
                # insert v2
                curNew.next = cur2
                # update cur2
                cur2 = cur2.next
            # we just inserted a node, so update curNew
            curNew = curNew.next

        # if one list still has unmerged nodes - append the whole list
        if cur1:
            curNew.next = cur1
        if cur2:
            curNew.next = cur2
        # return the head - this will be the first node we inserted into new list
        return newList.next
