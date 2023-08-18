
class Solution:
    """ 
        - the issue with a delimeter is that it could come up in the string itself
          and we can use a 2 char delimeter, but that could still come up etc
        - an alt way to encode the strings such that they can be 
          decoded is to keep an array that stores the length of each 
          string so we can decode it without a delimeter, but the 
          instrcutions say not to use any state variables
        - we can still store the length of each string, but it must be stored
          in the encoded string itself such that we dont use an additional data structure
        - we will store the length right before each string, with a delimeter between
          the length and the string itself
        - so we're still using a delimeter, but we can differentiate if its part of the string
          since the length tells us
    """
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # create a variable to store the encoded string
        result = ""
        # for each string
        for s in strs:
            # append the length of the string to the result
            result += str(len(s))
            # append the delimeter
            result += '#'
            # append the string itself
            result += s
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # make a variable for a list of strings
        result = []
        # track what position we're at in the string
        i = 0
        # iterate through the entire string
        while i < len(str):
            # make a pointer to track where the delimeter is
            j = i
            # find the next delimeter
            while str[j] != '#':
                j += 1
            # after finding the delimeter, we know the length value starts at i and ends at (not including) j
            # so get the length by doing i through j and convert to int
            length = int(str[i:j]) # this will exclude j from the range
            # the string starts after j and goes until j + length
            # so we can get the entire string using that range
            currentString = str[j + 1 : j + 1 + length] # this range excludes j + 1 + length
            # add the decoded string to the result array
            result.append(currentString)
            # now we need to update i to start at the next string
            i = j + 1 + length # this will give the first char of the length of next string
        return result




