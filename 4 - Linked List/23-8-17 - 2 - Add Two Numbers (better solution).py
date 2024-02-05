
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """ 
            - Digits of nums are in reverse order in the list which is
              actually easier for extracting the num from the list.
            - We can just use carry addition to add a corresponding digit 
              from each list and put the result into a new list
        """
        # track current ptr in each input list
        cur1, cur2 = l1, l2
        # get a starter burner node and a cur ptr
        burner = ListNode(0, None)
        cur = burner # cur ptr for result list
        # we also have to track carry
        carry = 0
        # while at least one list still has digits or we still have a carry to add
        while cur1 or cur2 or carry:
            # Note: if one list has finished bc there were less digits, we still need a value but it is 0
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            # get the result of addition (add both digits and any carry we may have from a previous calculation)
            result = v1 + v2 + carry
            # calculate the next carry (if num is greater than 9)
            carry = result // 10 # integer division rounds down. so if num > 9 we get a 1 for carry
            # remove carry from result
            result = result % 10
            # create a new node for the digit
            cur.next = ListNode(result, None)
            # shift ptr in all 3 lists (only if the list hasn't already ended)
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        # return the start of the answer list
        return  burner.next





