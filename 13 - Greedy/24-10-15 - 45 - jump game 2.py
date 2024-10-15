class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        - given: list of ints
        - return: the minimum number of jumps required to reach the end index from index 0

        what we know:
        - the values in the list rep how far you can jump from that index
            - can jump less though
        - at least one possible path is gauranteed
        - values can be 0, but not negative
            - if a value is 0, you have to jump over that index

        intuition:
        - brute force:
            - check every possible path, but this is k^n, where k is the average value of the list
            - but we don't need to do this, because were trying the same path segments multiple times
        - Dijkstra's shortest path:
            - we can model the list as a graph, where the values are nodes, and the jumps they can make are edges
            - this is linear on N + E = n*k where k is the average of the values
        - cleaner solution:
            - BFS type approach
            - the first layer of the BFS is the starting node
            - the 2nd layer is all the nodes you can reach from the starting node
            - the 3rd layer is all the nodes you can reach from the 2nd layer
            - and so on until a layer reaches the end node
            - the shortest number of jumps is the amount of layers to reach the end node, excluding the starting layer

        - time: linear on N + E = n*k where k is the average of the values
        - space:
        """
        minJumpCount = 0 # use to count the number of layers before reaching end
        l, r = 0, 0 # use to track the current window (layer of BFS)

        # traverse the list
        while r < len(nums) - 1:
            farthest = 0
            # find the right bound of the next layer (the farthest you can jump to from this layer)
            for i in range(l, r+1):
                distance = nums[i] + i
                farthest = max(farthest, distance)

            # update the window of the next layer
            l = r+1
            r = farthest

            # increment the count of jumps
            minJumpCount += 1

        return minJumpCount