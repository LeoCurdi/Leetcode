class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        - given: a list of ints rep a hand of cards, an int rep the group size
        - return: whether the cards can be rearranged based on the parameters

        what we know:
        - the cards must be rearranged into groups, st each group is the given size
        - the groups must consist of consecutive cards
            - ex: 2,3,4
        - hand[i] is te value of card i
        - cards cannot be reused
        - all cards must be used
        - thus, if the number of cards isn't divisible by the group size, we already cant rearrange the cards

        intuition:
        - brute force:
            - try all possible splits of the list into subsets of length g
            - this would be 2^n * n
        - better:
            - sort the list
            - start from the first index
            - grab the first g consecutive values, put them into a subset, and remove them from the original list
            - repeat from index 0 of the modified list until the list is empty or we cant complete a g length subset
            - sorting is nlogn, but popping n elements from the front of a list would be n*n
        - even better:
            - how to remove the min element from a list in more efficient time then shifting the whole list?
                - use a min heap
            - what do we do when there are multiple same values in the hand?
                - the heap will feed us both of them back to back, which we don't want since we need consecutive values
                - use a hashmap to count the occurences of each value
            - only use the min heap to get the lowest value for the start of the next group
            - once we have first val, easily use the hashmap to check if the consecutive values are in
            - decrease the count of each val that was used for the group
            - if the count of the val goes to 0, we must pop it from the heap
                - if we're trying to pop a value from the heap that's not the min value,
                  we can just return false right there, because we know a future iteration
                  will not be able to complete the group
            - once the heap runs out of values, return true
            - if we fail to complete a group, return false
        - edge case:
            - check if the group size even works with the hand length before running the alg

        - time: nlogn for popping n elements from a min heap
        - space: n for the hashmap and heap
        """
        # edge case
        if len(hand) % groupSize != 0:
            return False

        # create a frequency counter
        countMap = {} # could use a counter in python, but a hashmap is better for code clarity in an interview
        for n in hand:
            countMap[n] = 1 + countMap.get(n, 0) # increase the count by 1, and use a default value in case it doesn't exist yet

        # create a min heap
        minHeap = list(countMap.keys()) # take the values, turn it into a list
        heapq.heapify(minHeap)

        # continue until min heap is empty (or we fail to complete a group)
        while minHeap:
            # get the first value of the next group
            first = minHeap[0]
            # use the hashmap to see if we can complete the group
            for val in range(first, first + groupSize):
                # if we can't complete the group
                if val not in countMap or countMap[val] == 0:
                    return False
                countMap[val] -= 1
                # if we can complete the group, but we must pop a value thats not the min for the next grou
                if countMap[val] == 0:
                    if minHeap[0] != val:
                        return False
                    heapq.heappop(minHeap)

        # we completed the groups
        return True

