class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        - given: an array of pairs of points x,y, and an int k
        - find: the k closest points to the origin (0,0)

        - how to compute distance?
        - are there duplicate points? no
        - what is the format for the answer? return in any order, need to return pairs

        - compute the distance for each point, and insert into a min heap (nlogn)
        - better solution: compute the distance for each point, then heapify the array in one shot (linear time)
        - pop and return the k shortest distances (klogn)

        -time: n + klogn = klogn for popping k points from the heap
        -space: n for the heap
        """
        # create a min heap
        minHeap = []

        # iterate each point
        for p in points:
            # compute dist
            dist = math.sqrt((p[0] ** 2) + (p[1] ** 2))
            # insert into the array
            minHeap.append([dist, p[0], p[1]])
        
        # heapify the array
        heapq.heapify(minHeap)

        # pop k smallest points into result
        result = []
        for i in range(k):
            p = heapq.heappop(minHeap)
            result.append([p[1], p[2]])

        return result