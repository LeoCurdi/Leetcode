class MedianFinder:
    """
    - brute force: insert each num in order (n*n) and easly find the median

    - better: use a heap
        - insert each num into the heap in log time
        - find the median by popping half the values, then push all the values back (n logn)

    - even better: use 2 heaps
        - divide the numbers equally into 2 heaps, one for the lower half and one for the higher half
        - the lower heap is a max heap, which gives the highest value of the lower half
        - the higher heap is a min heap, giving the lowest value of the higher half
        - the median is between those 2 nums
        - how to build 2 even heaps without overlapping values?
            - perform a balance each time a number is added to a heap
            - if the higher heap has more than 1 + the lower heap, pop the lowest and add it to the lower heap, adn vice versa

        - time: n logn for adding each num and balancing, and finding median is constant time
        - space: linear for inserting n nums into 2 heaps.   
    """

    """
    initializes medianFinder object
    """
    def __init__(self):
        # create a min heap for upper half and max heap (min heap with inverse nums) for lower half
        self.lowerMaxHeap, self.upperMinHeap = [], []
        
    """
    - given: and int num from the data stream
    - adds num to the medianFinder object
    """
    def addNum(self, num: int) -> None:
        # base case - adding the first num
        if not self.lowerMaxHeap and not self.upperMinHeap:
            # default it to the lower heap
            heapq.heappush(self.lowerMaxHeap, -1 * num)
        # if the num is greater then the max of the lower side, push it to the upper heap
        elif num > -1 * self.lowerMaxHeap[0]:
            heapq.heappush(self.upperMinHeap, num)
        # if the num is less or equal to the max of the lower side, push it to the lower heap
        else:
            heapq.heappush(self.lowerMaxHeap, -1 * num)

        print("added: ", num)
        print(self.lowerMaxHeap)
        print(self.upperMinHeap)  

        # check if heaps need to be balanced
        if len(self.upperMinHeap) > len(self.lowerMaxHeap) + 1:
            # upper heap is too big - pop a value and push it to the lower heap
            value = heapq.heappop(self.upperMinHeap)
            heapq.heappush(self.lowerMaxHeap, -1 * value)

        elif len(self.upperMinHeap) < len(self.lowerMaxHeap) - 1:
            # lower heap is too big - pop a value and push it to the upper heap
            value = -1 * heapq.heappop(self.lowerMaxHeap)
            heapq.heappush(self.upperMinHeap, value)  

        print("balanced ")
        print(self.lowerMaxHeap)
        print(self.upperMinHeap)          
        
    """
    - finds: the median of the numbers that have been added so far
    """
    def findMedian(self) -> float:
        print("finding mid, heaps: ")
        print(self.lowerMaxHeap)
        print(self.upperMinHeap)  

        result = 0
        # if one heap is larger, it has the median
        if len(self.upperMinHeap) > len(self.lowerMaxHeap):
            result = self.upperMinHeap[0]
        elif len(self.upperMinHeap) < len(self.lowerMaxHeap):
            result = -1 * self.lowerMaxHeap[0]
        # else the median is between the 2 middle values
        else:
            result = (self.upperMinHeap[0] + (-1 * self.lowerMaxHeap[0])) / 2

        return result


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()