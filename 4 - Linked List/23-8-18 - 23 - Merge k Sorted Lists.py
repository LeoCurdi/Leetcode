
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """ 
            - We can merge k sorted lists by merging 2 of them at a time 
              until the last 2 have been merged together
            - This is basically merge sort with linked lists
            - The time complexity will be o(NlogK) where n is the amount of nodes and k is the amount of lists

        """
        # Error handling
        if not lists or len(lists) == 0:
            # if there is nothing to merge just return null
            return None
        # while there's still lists to be merged (theres more than 1 list)
        while len(lists) > 1:
            # put the merged lists into a fresh array
            mergedLists = []
            # we're going to merge every pair of neighboring lists together (so if there's 8 lists we will end up with 4 after this iteration of the while loop)
            for i in range(0, len(lists), 2): # increase i by 2 at a time
                # grab the 2 unmerged lists that are next to each other
                l1 = lists[i]
                # we don't know there are still 2 unmerged lists so check
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # merge the lists with merge 2 lists function
                mergedList = self.merge2Lists(l1, l2)
                # add the result to our fresh array
                mergedLists.append(mergedList)
            # discard the old unmerged lists and replace it with the new merged lists
            lists = mergedLists
        # once lists length equals 1, that 1 list will be the final merged list
        return lists[0] # only return the list (not it's container)

    # write the function to merge 2 sorted lists (just copy the code from that leetcode question)
    def merge2Lists(self, l1, l2):
        # create a dummy node for head
        dummy = ListNode()
        # create a current (tail) pointer
        tail = dummy
        # create cur ptrs for each list
        cur1 = l1
        cur2 = l2
        # while both lists still have nodes to be merged
        while cur1 and cur2:
            # merge the lesser node
            if cur1.val < cur2.val:
                # merge node
                tail.next = cur1
                # update ptr
                cur1 = cur1.next
            else:
                # merge node
                tail.next = cur2
                # update ptr
                cur2 = cur2.next
            # update new list cur ptr
            tail = tail.next
        # if one of the lists still has nodes - append the whole thing to the new list
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        # return the head of the new list (the node after dummy)
        return dummy.next

