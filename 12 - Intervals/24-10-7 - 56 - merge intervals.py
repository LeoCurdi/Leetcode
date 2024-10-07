class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        - given: an array of intervals
        - return: the array, but with all overlapping intervals merged

        what we know:
        - interval i = [starti, endi]
        - if an interval starts at the same time another interval ends, they count as overlapping and can be merged
        - the given examples are sorted by start time, but it's not a given

        intuition:
        - sort the intervals by start time
            - will make checking much easier
            - this will come at a time complexity penalty
        - iterate through each interval in order
            - compare the end time of interval i to the start of i+1
            - if they overlap, merge them
                - the current interval will take the min of si and si+1, and the max of ei and ei+1
            - if not, place it into a result array

        - time: nlogn for sorting, the main alg would be linear
        - space: linear for creating a new result list
        """
        # sort the intervals
        intervals.sort(key=(lambda pair: pair[0])) # use an anonymous function to sort by first element in each pair

        # iterate through the list
        result = []
        cur = intervals[0]
        for i in range(len(intervals)-1): # boundary case
            next = intervals[i+1]
            # if the current interval doesnt overlap the next
            if next[0] > cur[1]:
                # clear it into the result
                result.append(cur)
                # shift cur for the next iteration
                cur = next
            # otherwise if there is overlap
            else:
                # merge the next one into cur
                cur = [min(cur[0], next[0]), max(cur[1], next[1])]

        # we need to add in the final interval
        result.append(cur)
            
        return result

