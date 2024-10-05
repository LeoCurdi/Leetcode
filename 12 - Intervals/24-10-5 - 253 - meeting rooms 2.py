class Solution:
    """
    Definition of Interval:
    class Interval(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        """
        - given: an array of meeting time intervals
        - return: the minimum number of separate rooms required

        what we know:
        - a meeting time i = [si, ei] where s is the start time and e is the end time
        - an interval is an object, whos definition is given above
        - if multiple meetings take place at the same time, separate rooms are necessary
        - we need to find out whats the max number of meetings happening at the same time
        - if a meeting ends and another starts at the same time, they are not considered overlapping

        intuition:
        - brute force approach:
            - we could run a simulation of meetings over time
            - have a while loop that runs from time 0 until all meetings are done
            - start and end meetings when we reach the correct times
            - check how many meetings are open at any given time
            - this approach is n*k where n is the amount of meetings and k is the time difference until all meetings are done
        - optimized solution:
            - same idea as brute force, but we don't need an iteration for every time unit
            - we can jump to times that have a meeting starting or ending
            - also, we don't need to even know what meetings were starting or ending,
              we just need to keep track of how many meetings have started vs ended
        - how to handle ties in start and end times?
            - process end times before start times, so that we close a meeting before opening the next one, so we don't count them running at the same time
        - how to iterate over start AND end times efficiently
            - we need to sort by both start and end time
            - put them into separate arrays

        - time: nlogn for sorting, iterating over all the times would be linear
        - space: linear to put all times into separate memory
        """
        startTimes = sorted([i.start for i in intervals]) # grab all start times in sorted order
        endTimes = sorted([i.end for i in intervals])

        """
        startTimes, endTimes = [], []
        for i in intervals:
            startTimes[i] = i.start
            endTimes[i] = i.end

        startTimes.sort()
        endTimes.sort() """

        result, curCount = 0, 0
        s, e = 0, 0 # pointer for current start and end times

        # iterate all times
        while s < len(startTimes):
            # compare cur start and end
            if startTimes[s] < endTimes[e]:
                # open a meeting
                curCount += 1
                s += 1
            else: # if their equal we want to close a meeting first
                # close a meeting
                curCount -= 1
                e += 1
            # update result
            result = max(result, curCount)
        
        return result



