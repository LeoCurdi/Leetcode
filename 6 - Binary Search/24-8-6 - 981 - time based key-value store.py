class TimeMap:

    def __init__(self):
        # create a hashmap
        self.store = {} # key = string, value = list of pairs ([[value1, time1],...])
        
    """
    - appends a <value,time> pair to the list of values associated with a specific key
    - note: time stamps are always given in increasing order
    - time: constant for inserting a value at the end of a list
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if the key is in the hashmap
        if key not in self.store:
            self.store[key] = [] # give the new key an empty list to start
        # append the value/time pair
        self.store[key].append([value, timestamp])

    """
    - searches (binary search) for the provided timestamp in the list of values associated 
    with the provided key, and returns the value corresponding to the timestamp, 
    or the previous value if the timestamp is not found
    - time: logn for binary search
    """
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # get the list of values
        values = self.store.get(key, []) # return empty list if key not found
        
        # run binary search
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] == timestamp:
                result = values[middle][0]
                break
            elif values[middle][1] > timestamp:
                right = middle - 1
            else:
                result = values[middle][0]
                left = middle + 1
        
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)