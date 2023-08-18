
class LRUCache(object):
    """ 
        - This is more of a design problem then an algorithms problem
          and it is a common interview question
        - A least recently used cache is a cache that tracks and removes 
          least recently used items when it runs out of space.
          It is similar to how internet browser caches work
        - We're gonna use a hashmap to store and instantly look up values.
          We'll also need to implement a linked list such that we can reorder
          values in constant time vs an array. Reordering is essential so we 
          can put the most recently used to the front and let the lru fall back.
          We need the list to be doubly linked.
          The hashmap will store a key and a pointer to the node containing the value.
          When capacity is hit we will remove the last node.

    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # capacity
        self.capacity = capacity
        # hashmap
        self.cache = {} # [key: node] node contains value
        # init a couple dummy nodes which provide a buffer for edge cases when the list has less than 2 values
        # dummy nodes make insert and remove so much smoother
        self.head = Node(0, 0) # default values
        self.tail = Node(0, 0)
        # connect the dummy nodes together
        self.head.next = self.tail
        self.tail.prev = self.head
    # head.next = LRU, tail.prev = MRU

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if the key exists - return the value AND update it to most recently used
        if key in self.cache:
            # update value to most recently used by removing it and re-inserting it at tail (MRU)
            # make a couple helper functions to remove and insert
            self.remove(self.cache[key]) # self.cache[key] = node
            self.insert(self.cache[key])
            return self.cache[key].value # self.cache[key] gives us a node
        # if it doesnt exist - return -1
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if we have a key that's already in the cache - we want to overwrite it
        # so just remove it for now then we can re insert later
        if key in self.cache:
            self.remove(self.cache[key])
        # create the new node and put it in the cache with the key
        self.cache[key] = Node(key, value)
        # insert the node into the list
        self.insert(self.cache[key])
        # this is the important part
        # if we've exceeded the allotted space for the cache - we must remove the LRU
        if len(self.cache) > self.capacity:
            # grab the LRU node
            lru = self.head.next
            # remove the node
            self.remove(lru)
            # remove the value from the hashmap (we don't need to remove the key as it will just be empty after we remove the value)
            del self.cache[lru.key]

    # remove a node from wherever it is in the list
    def remove(self, node):
        # prev and next ptrs
        # we dont need to check if they exist bc we made dummy nodes that will always exist
        prev = node.prev
        nxt = node.next
        # modify links
        prev.next = nxt
        nxt.prev = prev

    # insert a node to end of list (MRU)
    def insert(self, node):
        # get prev and next ptrs
        prev = self.tail.prev # tail is a dummy so get the one before that
        nxt = self.tail # dummy will stay to the right
        # link up the node
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

# make a node class
class Node:
    # accept a key and a value
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None