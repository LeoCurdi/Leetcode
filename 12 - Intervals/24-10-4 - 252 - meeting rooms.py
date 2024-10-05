class Solution:
    """
    Definition of Interval:
    class Interval(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
    """
    def canAttendMeetings(self, intervals):
        """
        - given: an array of meeting times
        - return: whether a person could attend all meetings

        what we know:
        - a meeting time is as follows: intervals[i] = (start time, end time)
        - we can assume that a person can teleport from one meeting to the next without taking extra time in between

        intuition:
        - if a person is going to attend all meetings, the only requirement is that none of the times overlap
        - brute force approach:
            - sort based on start times
            - for each end time ei, check each start time starting from s(i+1) until sn
            - if any of the subsequent start times are less than ei, there is a time conflict
            - this approach is n*n, where n is the number of meetings
        - optimization:
            - since the start times are sorted in increasing order,
              for each end time ei, we only need to check 1 start time s(i+1)
            - if that start time comes after the prev end time, we know all subsequent ones will too since they must be greater
            - this cuts it down to only n comparisons
            
        - time: nlogn for sorting the input
        - space: depends on the sorting implementation
        """
        # sort the intervals in ascending order by start time
        intervals.sort(key = lambda i : i.start) # lambda is an anonymous function. sort based on the start value of each interval

        # for each end time from 0 to n-1
        for i in range(len(intervals) - 1):
            ei, sj = intervals[i].end, intervals[i+1].start # intervals is an object
            # check end time e against start time e+1
            if ei > sj:
                return False
            
        return True