class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        - given: a number of courses, a prerequisites array
        - return: an order to take the courses in s.t. you can finish all of them

        what we know:
        - if prereqs[i] = [1,0], then you have to take course 0 before 1
        - the course names go from 0 to numCourses-1
        - like course schedule 1, where we need to find a way to complete all courses
        - there may be multiple correct solutions, just return one of them
        - if there are none, return an empty list

        intuition:
        - using the same logic from course schedule 1, if there's a way to complete the courses, we can find it
            - model the course roadmap as a graph
            - if there is a loop in the graph, then its impossible
            - ex: [1,0],[2,1],[0,2]        
        - we just need to find a way to record the path that allowed us complete them
            - use topological sort, which gives a valid ordering for traversing a graph in order
                - a dfs variation
                - when you reach a class with no pres, add it to the output
                - then mark it visited, and remove it from the pres list of parent class
            - use a hashmap to map each course to its list of pres
        
        - time: O(n+e) where n is numCourses and e is num pres, since we cut out repeated work by skipping visited courses
        - space: O(n) for the depth of the call stack
        """
        preMap = {i:[] for i in range (numCourses)} # pre init the map since we know what keys were inserting
        visitedNodes = set() # for cycle detection (remember the current path)
        result = []


        # fill the map with all pres
        for a, b in prerequisites: # a requires b
            preMap[a].append(b)

        # define a helper function for dfs (returns true if a cycle is found)
        def dfsHelper(i):
            # base case: course i was already completed
            if i in result:
                return False # return false for no cycle

            # base case: course i has no pres
            if preMap[i] == []:
                result.append(i) # add it to the result
                return False # return false for no cycle

            # base case: cycle detected
            if i in visitedNodes:
                return True # return true for cycle detected

            # call dfs on each pre of i
            visitedNodes.add(i)
            for p in preMap[i]:
                if dfsHelper(p):
                    return True # if a cycle was detected, propagate it up
            visitedNodes.remove(i) # clean up

            result.append(i) # add it to the result
            return False # no cycle detected, could complete the course


        # call dfs on each node, to ensure we dont miss any components of the graph
        for i in range(numCourses):
            if dfsHelper(i):
                return [] # if a cycle was detected, we couldnt complete all courses

        return result