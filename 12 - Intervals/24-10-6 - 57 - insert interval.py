class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        - given: an array of intervals, a new interval
        - return: the intervals list with the new interval added

        what we know:
        - the intervals do not over lap
        - interval i = [start i, end i]
        - intervals is sorted in ascending order based on start

        - the new interval must be inserted in order by start
        - if it causes an overlap with another interval, they must be merged
        - if there is a tie (an end time is the same as another interval's start time):
            - it counts as overlap and should also be merged

        intuition:
        - inserting in order is easy, just do a binary search to find the index to insert into
            - or just do a linear search, since it doesn't effect overall time complexity and its easier
        - how to detect which intervals overlap?
            - for intervals whos start time comes before new:
                - these are left of the new index
                - we just need to check their end times against the new start time
                - optimization: we now there are no pre-existing overlaps, 
                  so there can only be one left interval that overlaps the new interval
            - for intervals who start after new:
                - these are right of the new index
                - we need to check their start time against the new end time
        - how to merge intervals?
            - pop them from the list
            - update the start/end of the new interval
                - check for new min/max
        - CLEANER SOLUTION:
            - iterate over the list once
            - insert each interval into the result, until we start hitting overlap
            - for overlap, merge the intervals together
                - just update the bounds of new
            - once were past the overlap, insert new, then insert the rest of the intervals

        - time: linear to iterate over the list of intervals once
        - space: linear to create a separate result list
        """
        result = []

        # find the index to insert the interval into
        for i in range(len(intervals)):
            # case: the interval has been properly merged in, and the remainder of the intervals are untouched
            if intervals[i][0] > newInterval[1]:
                # insert interval, then append the rest of the intervals and were done
                result.append(newInterval)
                return result + intervals[i:]
            # case: we havent reached any overlap yet, and thus the current interval i is ok
            elif intervals[i][1] < newInterval[0]:
                # insert old interval as is
                result.append(intervals[i])
            # overlap case
            else:
                # we need to update the bounds of the new interval to absorb the old one
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # we want to toss the old interval, so just do nothing

        # case; new interval ended up going at the end
        result.append(newInterval)            

        # return the new list
        return result