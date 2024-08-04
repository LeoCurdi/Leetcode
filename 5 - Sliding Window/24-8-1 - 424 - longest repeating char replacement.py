class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - given: an uppercase string and an int k
        - find: the longest single char substring that can be created by replacing up to k chars
        
        - sliding window
        - use hashmap to count the number of occurences of each char in the window
        - compute the most frequent char in the window
        - check if k is high enough to replace all other chars
            - if not, shorten the window
            - else, lengthen the window

        - time: one pass, so linear
        - space: we have a hashmap, but its bounded by the size of the alphabet, so constant
        """
        result = 0
        hashMap = {}
        left = 0

        for r in range(len(s)):
            # add the count of the newest char to the hashmap
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1

            # if the window isn't valid (there are more than k unmatching chars), shrink the window
            while (r - left + 1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1 # remove from count
                left += 1

            # update the result
            result = max(result, r-left+1)

        return result