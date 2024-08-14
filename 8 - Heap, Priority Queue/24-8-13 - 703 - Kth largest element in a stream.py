class KthLargest:
    """
    - given: an int k and a list of integers

    - time: n*logn for building the heap then popping all but the top k elements
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # create a min heap to only store the k largest elements from the list, with the Kth as the top (min)
        # this works because we never need to remove elements
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    """
    - given: an int
    - adds the int to the list of nums and returns the kth largest in the list
    - it is gauranteed that there will be at least k elements when add is called

    - time: logn for adding and popping an element
    """
    def add(self, val: int) -> int:
        # add the new value to the min heap
        heapq.heappush(self.minHeap, val)
        # if there are now more than k elements, pop one
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # return the kth largest (the min of the heap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)