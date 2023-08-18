
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """ 
            - we're gonna use the 2 pointer strategy
            - Start with a left and right, close in on the center.
              If at any point the chars dont match, return false.
              If we make it all the way to the middle without a mismatch, return true
            - Check each char for alphanum. If false, skip the char as it is meant to be excluded
        """
        # set up left and right pointer
        l = 0
        r = len(s) - 1
        # iterate towards the middle
        while l < r:
            """ 
                Note: we are only skipping 1 non alphanum char per iteration here.
                We could switch the ifs for while loops to skip all non alphanums in the
                event there are multiple in a row
            """
            # if left is not alphanum, skip it
            if not self.isAlphanum(s[l]):
                l += 1
            # else if right is not alphanum - skip it
            elif not self.isAlphanum(s[r]):
                r -= 1
            # else (both are now alphanum) if they dont match - return false
            # make sure to lowercase any uppers as we are ignoring case
            elif s[l].lower() != s[r].lower():
                return False
            # else shift pointers inwards and continue
            else:
                l += 1
                r -= 1
        
        # if we make it to the middle, return true
        return True

    
    # write a function to check if a char is alphanumeric
    def isAlphanum(self, c):
        # return true or false
        return (
            # use ord to get ascii value
            # check if its an uppercase letter,
            ord('A') <= ord(c) <= ord('Z')
            # or a lowercase letter,
            or ord('a') <= ord(c) <= ord('z')
            # or a number
            or ord('0') <= ord(c) <= ord('9')
        )
