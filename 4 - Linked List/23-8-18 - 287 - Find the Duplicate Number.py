
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ 
            - Note: this problem is the ultimate test of whether you've 
              seen the problem or not lol. It is still valuable tho because
              it does show up in interview quite a lot.
            - We can't use a hashmap to solve this problem as we must
              only use constant extra space. (otherwise it would be really easy)
            - If we sorted the list it would also be easy but we want a linear time solution
              and we can't modify the input array
            - These restrictions make it more like a leetcode hard
            - We're going to use something called Floyd's Cycle Detection 
              (there's no way you'd come up with this in a 30 minute 
              interview without having done it before)
            - Honestly just watch the neetcode video on it
            - Algorithm:
              - Turn the array into a linked list where the value at index i 
                says which index to go to for the next value.
              - Make a fast an slow ptr that start at head.
              - Shift both ptrs until they intersect.
              - Disregard the fast ptr.
              - Make another slow ptr starting at head.
              - Shift both slow ptrs until they intersect.
              - This intersection will always be the result
            - Good luck figuring that out without memorizing it.
        """
        # start with slow n fast ptrs at head (index 0 in array)
        slow, fast = 0, 0
        # infinite loop that will break once the ptrs intersect
        # Note: this is basically a do while loop bc we want to go until they intersect but they start off intersecting
        while 1:
            # move slow by 1 node
            slow = nums[slow]
            # move fast by 2 nodes
            fast = nums[nums[fast]]
            # go until they intersect
            if slow == fast:
                break
        # phase 2 - make a new slow ptr
        slow2 = 0
        # infinite while loop since python doesn't have a do-while
        while 1:
            # advance both slow ptrs
            slow = nums[slow]
            slow2 = nums[slow2]
            # go until they intersect
            if slow == slow2:
                break
        # the num that the slow ptrs intersected on is the answer
        return slow # nums[slow] would give the index of the next node so just return slow
            



