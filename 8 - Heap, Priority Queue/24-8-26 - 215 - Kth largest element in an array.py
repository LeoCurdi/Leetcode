class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        - given: an array of ints, and an int k
        - find: the kth largest element in the array

        - how is k formatted? if k = 1, we want the largest

        - could use a max heap, and pop k elements to find the result, but thats o(klogn)
        - better solution: use quickselect (similar to merge sort, but less repeated work)
            - partition the array based on a pivot
            - repeat on the subhalf containing the kth largest (if there are more than k elements in the upper half, so is the kth largest)
        - time: o(n + n/2 + n/4 + ... + n/n) = o(2n) = o(n), for partitioning the array each round
        - time worst case: o(n^2) when every partition choses the worst pivot

        - NOTE: this alg takes too long on large arrays where most of the numbers are the same,
            could be fixed using 3-way partition (Dutch national flag) to skip over all nums that equal the pivot,
            but I'm too lazy to write that up right now
        """
        # find the index of the result (if the array was sorted)
        kIndex = len(nums) - k
        # keep track of a window within the array
        left, right = 0, len(nums) - 1

        # repeat until the kth largest is found
        while left < right:
            # partition the array
            pivotIndex = self.partition(nums, left, right)
            # kth is right
            if kIndex > pivotIndex:
                left = pivotIndex + 1
            # kth is left
            elif kIndex < pivotIndex:
                right = pivotIndex - 1
            # kth is the pivot
            else:
                break
        
        return nums[kIndex]

    # well be partitioning multiple times, so we need a function for it
    # takes in the full array and a window, returns the pivot
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill
