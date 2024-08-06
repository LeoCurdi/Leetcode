class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - given: n piles of bananas, h hours
        - find: the minimum k such that koko can eat up to k bananas from any pile per hour and finish all bananas within h hours
        
        - brute force: try each k starting at 1
        - better: k is upper bounded by the max amount of bananas in a pile, so use binary search on the range until we reach the lowest k that works
        
        - time: log(max(p)) * P, where P is the number of piles and max(p) is the size of the largest pile
        """
        low, high = 1, max(piles)
        k = high

        while low <= high:
            middle = (low + high) // 2
            # compute time with current k
            hours = 0
            for p in piles:
                hours += math.ceil(p / middle) # need to round up
            # if the k is high enough to be valid - go for a lower k
            if hours <= h:
                k = middle # record the lower k
                high = middle - 1
            # if the k is not high enough
            else:
                low = middle + 1

        return k
