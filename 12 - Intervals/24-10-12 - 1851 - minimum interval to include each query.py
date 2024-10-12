class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        - given: a list of intervals, a list of queries
        - return: a list contianing the answers of each query

        what we know:
        - the size of an interval is the difference between start and end
            - size = e - s + 1
        - for each query j, the answer is:
            - the smallest interval that starts before or on j and ends on or after j
            - aka si <= j <= ei, where i is the shortest interval satisfying the condition
        - we want to record the sizes of each result interval
        - if no valid interval exists, record -1

        intuition:
        - we can sort the intervals by start for efficient iterating
        - we can generate a list containing the sizes of each interval so we don't have to repeat computation
        - brute force:
            - for each query, check every interval to see if its in range, and save the smallest size
            - this approach is n*m for checking all queries against all intervals
            - there is a slight optimization: once an interval starts after the query, we don't have to check any more
        - efficient solution uses minHeap
            - too confusing, watch the neetcode video
            - basically just adds all valid intervals to the heap, then takes the minimum
            - each time we get a new query, we pop intervals that are out of range and push the new in range ones

        - time: nlogn for sorting and pushing n intervals to a heap (which has logn access)
        - space: n for the extra memory for the heap
        """
        intervals.sort() # sort intervals by start value (python default)
        sortedQueries = sorted(queries) # create a copy of queries for sorting. we need the original order
        
        minHeap = []
        resultMap = {} # use a hashmap to map the queries to their results, so we can restore the original unsorted order
        interval = 0

        # for each query
        for q in sortedQueries:
            # add each interval to the heap, if it starts before the query
            while interval < len(intervals) and intervals[interval][0] <= q:
                s, e = intervals[interval]
                heapq.heappush(minHeap, (e - s + 1, e)) # add the interval to the heap. include size and end value
                interval += 1

            # pop each interval that ends before the the query
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # get the smallest valid interval from the top of the min heap
            resultMap[q] = minHeap[0][0] if minHeap else -1

        # convert the result to a list in the original unsorted order
        result = [resultMap[q] for q in queries]
        return result

