class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        - given: am array of CPU tasks, a cooling time n. one task can be completed per cycle. Identical tasks must be separated by at least n cycles.
        - find: the minimum number of cycles required to complete all tasks.

        - how long do tasks take to complete? each task takes exactly 1 cycle
        - how many types of tasks can there be? at most 26, since tasks must be uppercase english chars

        - we want to start working on the most repeated tasks first, since they require the longest total time to complete with cooldowns between
        - iterate through to create a frequency table of how many times each task is repeated
        - use a max heap to continuously get the highest priority task to complete
        - we can also use a queue and a timer to keep track of when a task's cooling time is up
            - pop the max value from the heap, run the task, decrement the quantity remaining, and add it to the queue
            - when a task has no cooling time left, pop it from the queue and push it to the heap
        - we dont need to keep track of which task is which, just the quantities remaining since we just need to find the total time
        - use a min heap with negative values since python doesn't support max heaps

        - time: linear for counting frequencies, heapify, and processing each task
        - space: linear for adding the input to a counter, a heap, and a queue
        """
        curTime = 0
        queue = deque() # [-task freq, time when cooling is up]
        # count the frequency of each task and push it to the heap
        freq = Counter(tasks) # Counter is Python's built in way of inserting each element into a hashmap to get the counts
        taskMinHeap = [-c for c in freq.values()] # add negative freq values to the heap
        heapq.heapify(taskMinHeap) # turn it into a heap
        # loop until finished processing
        while taskMinHeap or queue:
            curTime += 1

            # heap contains all tasks that are ready
            if taskMinHeap:
                # process a tasks
                t = heapq.heappop(taskMinHeap)
                t += 1 # add 1 to the quantity of the task remaining, since were working with negative values

                # add the task to the queue, with the time when cooling is up
                if t != 0: # except when quantity hits 0, then the task is done
                    queue.append([t, curTime+n])

            # the queue will end up being ordered by highest quantity task to lowest, so we only need to check the first task in the queue
            if queue and queue[0][1] == curTime: # check if cooling is up
                # if so, add it to the heap since its ready
                t = queue.popleft()
                heapq.heappush(taskMinHeap, t[0]) # just add the quantity

        # return the number of cycles required (total time accumulated during the most efficient processing order)
        return curTime