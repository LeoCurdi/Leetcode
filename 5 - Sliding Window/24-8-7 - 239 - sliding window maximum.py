class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        - given: an array of ints, a length k sliding window moving left to right, you can only see the nums within the window
        - find: a list containing the max value from the sliding window at each position in the array

        - easy solution: just scan the window for the max at each iteration, but that is o(k*(n-k))
        - better: 
            - eliminate the repeated work by:
                after finding the max of the current window, never check the values to the left of that max again
            - we can use a deque to insert new values from the right and drop values from the left that cannot be maxes anymore
            - the deque will always be monotonically decreasing, since we will always eliminate elements to the left of local maxes
        
        - time: o(n) for adding and removing every element from the deque once
        - space: o(n) for the deque
        """
        result = []
        # insert the initial window into the deque, popping lower values, which could no longer be maxes
        dq = collections.deque()
        for i in range(k-1): # the last initial value will be inserted in the first main loop iteration
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        left = 0
        for right in range(k-1, len(nums)):
            # insert the new right into the deque, after popping lower values, which could no longer be maxes
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            # record the max
            result.append(nums[dq[0]])
            # update left
            left += 1
            # check if the current max just moved out of bounds
            if dq[0] < left:
                dq.popleft()

        return result