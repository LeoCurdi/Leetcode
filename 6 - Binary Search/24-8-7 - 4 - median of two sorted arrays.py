class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        - given: 2 sorted arrays
        - find: the median (middle) value between the 2
        
        - merging is linear time, so its not an option
        - the only thing we can do in log time is binary search
            - get the middle of both arrays to get the left half of each
            - check the edge values against each other to see if the partition is correct if the arrays were merged
            - if not, adjust the pointers of the array with the lower middle to the right and the other array to the left until the partitions are correct

        """
        totalSize = len(nums1) + len(nums2)
        half = totalSize // 2 # rounding half down
        
        # swap the arrays such that we run the binary search on the shorter one
        n1, n2 = nums1, nums2
        if len(n1) > len(n2):
            n1, n2 = n2, n1

        # run binary search on array 1 to find the perfect partition between both
        l, r = 0, len(n1) - 1
        while True:
            mid1 = (l + r) // 2
            mid2 = half - (mid1 + 1) - 1 # use the global half to compute the middle of array 2

            # get the edge values, and give a default value for edge cases when indices are out of bounds
            left1 = n1[mid1] if mid1 >= 0 else float("-infinity")
            right1 = n1[mid1+1] if mid1 < len(n1)-1 else float("infinity")
            left2 = n2[mid2] if mid2 >= 0 else float("-infinity")
            right2 = n2[mid2+1] if mid2 < len(n2)-1 else float("infinity")

            # check for correct partition
            if right1 < left2:
                # we need more of nums1 in the partition
                l = mid1 + 1

            elif right2 < left1:
                # we need less of nums1 in the partition
                r = mid1 - 1

            else:
                # we got the right partition, so we can return the median here
                # if total size is even, we need max(left partition) + min(right partition) / 2
                if totalSize % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                # if total size is odd, we need min(right partition)
                else:
                    return min(right1, right2)
                
        n1, n2 = nums1, nums2
        totalSize = len(nums1) + len(nums2)
        half = totalSize // 2

        if len(n2) < len(n1):
            n1, n2 = n2, n1

        left1, right1 = 0, len(n1) - 1
        while True:
            i = (left1 + right1) // 2  # A
            j = half - (i + 1) - 1  # B

            Aleft = n1[i] if i >= 0 else float("-infinity")
            Aright = n1[i + 1] if (i + 1) < len(n1) else float("infinity")
            Bleft = n2[j] if j >= 0 else float("-infinity")
            Bright = n2[j + 1] if (j + 1) < len(n2) else float("infinity")

            # partition is correct

            if Bleft > Aright:
                left1 = i + 1
            elif Aleft > Bright:
                right1 = i - 1
            else:
                # odd
                if totalSize % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # even
                else:
                    return min(Aright, Bright)