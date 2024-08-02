class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        - given: array of ints, one of them appears multiple times
        - find: the duplicate

        - easy way: use hashmap, but we cant use extra space
        - use floyd's tortoise and hare alg (linked list cycle detection)
            - this alg works here because there are n+1 nums but they are only in a range of 1-n, so every number in the array can be treated as an index of another
        - if there are multiple of the same num, they will point to the same index, thus at some point there will be a cycle
        """
        slow, fast = 0, 0

        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # now the pointers intersect - create a new slow pointer at the start and when the slow ptrs intersect, that is the duplicate
        slow2 = 0        
        while 1:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        