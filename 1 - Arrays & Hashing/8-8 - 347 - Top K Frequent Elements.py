
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """ 
        - k is within the number of unique elements, the answer is unique, we may return the answer in any order
        - strategy: o(N)
            - count the frequency of each num - o(N)
            - Option 1: use a max heap to return the k most frequent nums - o(K*logN). (we could sort but thats o(NlogN) and k may be smaller)
            - Option 2: use a bucket sort variation where we put each value in a hashmap with the key being that value's frequency o(N)
            - we use option 2 because its o(N) time (and o(N) space)
        """
        # create a frequency counter object
        count = {}
        # frequency hashmap (only needs to be as big as the input array bc the most we can have of 1 number is the same as the size of the array)
        # the index will be the frequency and the sub array at the index will be the list of nums with that frequency
        hashMap = [[] for i in range(len(nums) + 1)] # make an empty sub array for each possible frequency
        # go through each value in nums and count how many times it occurs
        for n in nums:
            # count each num
            count[n] = 1 + count.get(n, 0) # add 1 to count, and if count doesn't exist set it to 0 first
        # go through each value that we counted and put them in the hashmap
        for n, c in count.items(): # this wil return each key value pair
            # add the number to the hashmap with the key being it's frequency
            hashMap[c].append(n)
        # make a result array
        result = []
        # iterate until we've recorded the top k nums
        # start with i at the end of the hashmap and work backwards
        # Note: this nested for loop is still o(N) bc its only iterating over N elements in total
        for i in range(len(hashMap) - 1, 0, -1):
            # make an inner loop for when there's multiple numbers with the same frequency
            for n in hashMap[i]:
                # record the number
                result.append(n)
                # if we've reached k numbers, stop
                if len(result) == k:
                    return result

