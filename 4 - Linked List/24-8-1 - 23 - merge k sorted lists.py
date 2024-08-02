# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        - given: array of k linked lists, all lists are sorted
        - find: an alg to merge all the lists into one sorted list

        - write a function to merge 2 sorted lists
        - then merge lists in pairs of 2 until all lists are merged into one (like mergesort)

        - time: nlogk where k is the number of lists
        """
        # cover edge cases
        if not lists or len(lists) == 0:
            return None
        
        # perform a merge sort until all lists have been merged into one
        while len(lists) > 1:
            mergedLists = [] # temp array
            # merge all pairs of 2
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedList = self.merge2Lists(list1, list2)
                mergedLists.append(mergedList)
            # update the new set of lists
            lists = mergedLists
        return lists[0]

    def merge2Lists(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        # merge the lists in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1= list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # append the rest of the leftover list
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next
