
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # short ciruit - check if strings are different lengths
        if len(s) != len(t):
            return False
        # set up 2 frequency counter objects
        countS = {}
        countT = {}
        #countS, countT = {}, {} # optional python shorthand for the above
        # iterate through the strings
        for i in range(len(s)):
            # add each char to the count for both strings
            countS[s[i]] = countS.get(s[i], 0) + 1 # short circuit - add one to the count, but if count is undefined set it to 0 first
            countT[t[i]] = countT.get(t[i], 0) + 1
        # if the frequency counters are equal return true. else return false
        return countS == countT
        