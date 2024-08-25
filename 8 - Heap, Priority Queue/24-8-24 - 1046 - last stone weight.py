class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        - given: an array of ints, rep. the weights of stones. 
            a game where on each turn, the 2 heaviest stones are smashed together.  
            the lighter stone is destroyed, and the heavier stone's weight is 
            decreased by the weight of the lighter stone. until 1 stone is left
        - find: the weight of the last stone

        - use max heap.
        - each turn, pull the 2 heaviest stones, then compute and re insert the result of the turn
        - continue until there is < 2 stones left

        - time: nlogn for playing n rounds and popping / pushing a heap each time

        - NOTE: this solution uses heapq's private max heap functions, which are discouraged. see below for proper solution
        """
        # build the heap (linear time)
        heapq._heapify_max(stones)

        # game loop
        while len(stones) > 1:
            # get 2 heaviest
            stone1 = heapq._heappop_max(stones)
            stone2 = heapq._heappop_max(stones)
            # compute the weight difference
            remainder = stone1 - stone2
            # if they weren't equal, the heavier survives
            if remainder:
                heapq._heappush_max(stones, remainder)
        
        # return result - weight of last stone, or 0 if no stone remains
        return stones[0] if stones else 0
    
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        - alt solution using min heap with negation
        """
        # build the heap (linear time)
        # in python, we have min heap, which we can hack to be a max heap by using the negative of each stone weight instead
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # game loop
        while len(stones) > 1:
            # get 2 heaviest
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            # if one stone is heavier, it survives
            if abs(stone1) > abs(stone2):
                heapq.heappush(stones, stone1 - stone2) 
            # if stones are equal, they both break
        
        # return result - weight of last stone, or 0 if no stone remains
        return abs(stones[0]) if stones else 0
