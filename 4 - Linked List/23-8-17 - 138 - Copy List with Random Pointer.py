
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        """ 
            - All we have to do is create a deep copy of the list. It
              is however really hard because we're creating new nodes and we cant
              set up the random pointers to nodes that haven't been created yet
            - We're going to use a 2 pass approach to get the random pointers set up.
              The first pass we create all new nodes but don't link anything up, 
              and use a hashmap to map the original nodes to the new nodes.
              The second pass we'll use the hashmap to implement the random pointers
        """
    # create a hashmap object
        # add in null to point to null to cover edge cases where we put in an null node for the key
        hashMap = {None: None} # {oldNode: copyNode}
    # iterate through the linked list once, creating all new nodes and putting them in the hashmap
        # set up a current pointer
        cur = head
        # go until the current ptr reaches the end
        while cur:
            # create a new node with the node constructor and give it the same value
            copy = Node(cur.val)
            # map the current node to it's new copy
            hashMap[cur] = copy
            # shift
            cur = cur.next
    # iterate a second time and set next and random pointers
        # reset current ptr
        cur = head
        # go until end
        while cur:
            # get the copy of the current node
            copy = hashMap[cur]
            # set the next ptr - we have to access the hashmap to get the copy node vs the original node
            copy.next = hashMap[cur.next]
            # set the random ptr (this is the tricky part)
            copy.random = hashMap[cur.random] # this gives us the copy of cur.random
            # shift
            cur = cur.next
        # return the head of the deep copy
        # We've copied a bunch of nodes and linked them up, but we didn't 
        # save a pointer to the first copied node. So we need to access it with the hashmap
        copyHead = hashMap[head]
        return copyHead



