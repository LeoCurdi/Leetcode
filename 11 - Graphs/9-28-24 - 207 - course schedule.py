class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - given: a number of courses, a 2d array of prereqs representing the order you must take courses in
        - return: whether it is possible to finish all courses

        what we know:
        - if prereqs[i] = [0,1] then you have to take course 1 before 0
        - if prereqs contradict, ex [0,1] and [1,0] then it is impossible to finish all courses

        intuition:
        - draw out the list of classes as a roadmap, with arrows rep. prereqs
            - if class b requires a first, the arrow points from b to a
            - if a class doesnt have any outward arrows from it, it doesnt require any prereqs 
        - it becomes apparent that courses can be modeled as a graph
        - we know that to be impossible, we must have contradicting prereqs
        - contradicting prereqs appear as a cycle on the graph
            - ex: [1,0],[2,1],[0,2] you have to take 0 before 1, 1 before 2, and 2 before 0
        - so all we need is cycle detection
        - how to construct the graph?
            - use a hashmap
            - for each course, map it to a list of all of its prereqs
        - how to cover the whole graph (it may have separate components)?
            - for each course (0 to n-1), run dfs starting from that course
                - this will ensure we dont miss any separate components of the graphj
            - when returning to the node, we can pop prerequisites after visiting them and verifying they can be completed
                - this will prevent repeated work
        - how to detect cycles?
            - when running dfs, keep track of visited nodes
            - if you visit the same node twice, there must be a cycle
            - need to reset the visited list for each initial dfs call
            
        - time: O(n + e) where n is the number of classes, and e is the number of prerequisite pairs, since were avoiding repeated work
        - space: O(n + e) for putting everything into a hashmap
        """
        visitedNodes = set() # could also use an array
        prereqMap = {i:[] for i in range(numCourses)} # since we know were inserting 0 to n-1 courses, we can initialize them right off the bat

        # construct the hashmap
        for a, b in prerequisites:
            prereqMap[a].append(b) # a has b as a pre

        def dfsHelper(i):
            # base case: course doesnt have any pres
            if prereqMap[i] == []:
                return True # true means can complete
            
            # check for cycle
            if i in visitedNodes:
                return False # false means cannot complete
            
            visitedNodes.add(i)
            # branch to all pres
            for p in prereqMap[i]:
                res = dfsHelper(p)
                if not res:
                    return False
                prereqMap[i].remove(p) # pop the prereq from i's list, since its been completed
            visitedNodes.remove(i) # we should unvisit this node, because somewhere further up the dfs stack, we could make it back to this course from a different course requiring it

            return True

        # run a separate dfs starting from each course to make sure we cover the whole graph
        for i in range(numCourses):
            result = dfsHelper(i)
            if not result:
                return False
            visitedNodes.clear() # reset visited list
            
        return True

