class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        - given: a list of intervals
        - return: the minimum number of intervals you must remove to make the list have no overlaps

        what we know:
        - intervals that only touch at a point are not overlapping
            - ex: [1,2] and [2,3] are not overlapping
        - if 2 intervals are overlapping, we only necessarily need to remove 1
        - if more then 2 intervals are overlapping in the same cluster, we don't necessarily have to remove multiple
          so we must find the most optimal one(s) to remove

        intuition:
        - the input should be sorted to make iterating over it efficient
            - otherwise we'd need to check all of them against each other in n*n comparisons
        - when iterating, its easy to detect overlap
            - just check the endpoint of i against the start of i+1
        - the hard part is determining which interval to remove, 
          since we need to remove the one with the most overlaps
            - you can't just remove the longest one, since there are examples where a short inteval is overlapping multiple long intervals
            - you also cant just remove the one that starts first, it would depend on the example
        - notice that whichever interval ends last is going to have the most overlaps,
          so we should remove that one

        - time: nlogn for sorting, the rest is linear
        - space: constant, since were not using extra memory
        """
        countRemoved = 0
        # sort the list based on start
        intervals.sort(""" key = (lambda pair: pair[0]) """) # you can just sort without the key and python will sort based on start first then end if starts are equal

        # iterate the list
        i = 1
        while i < len(intervals):
            startCur, endCur = intervals[i]
            endPrev = intervals[i-1][1]
            # if overlap is detected
            if startCur < endPrev:
                countRemoved += 1
                # remove the one that ends later
                if endCur > endPrev:
                    # if the latter ends later, we need to remove it from the list
                    intervals.pop(i)
                    i -= 1
                # if the first one ends later, we can just skip it
            i += 1    
        
        return countRemoved