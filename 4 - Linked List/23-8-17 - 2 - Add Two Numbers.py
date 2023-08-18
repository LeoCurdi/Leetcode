
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
        """
    # get first num
        num1 = 0
        i = 1
        # traverse the list
        cur = l1
        while cur:
            # add the digit to the num by doing <digit * 10^i>
            num1 += i * cur.val
            # update i so the next digit will be 10 times larger
            i *= 10
            # shift
            cur = cur.next
        print(num1)
    # get 2nd num
        num2 = 0
        i = 1
        cur = l2
        while cur:
            num2 += i * cur.val
            i *= 10
            cur = cur.next
        print(num2)
    # add the nums
        result = num1 + num2
        print(result)
    # put it in a linked list
        dummy = ListNode(0, None)
        cur = dummy
        # edge case - result = 0
        if result == 0:
            return dummy
        while result:
            # get digit
            digit = result % 10
            # put it in a new node
            cur.next = ListNode(digit, None)
            # divide the result by 10
            result = result // 10
            # shift cur
            cur = cur.next
            print(dummy)
        # return the head of the new list
        return dummy.next




