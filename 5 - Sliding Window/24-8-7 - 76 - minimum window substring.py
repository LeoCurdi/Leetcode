class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        - given: 2 strings s and t
        - find: the minimum size substring of s that contains all chars in t
        
        - create a sliding window in s
        - create a freq table of t, and of the current window in s
        - iterate through s, updating the freq table
            - if the window contains all chars from t, 
                - record it as a potential result
                - shift the left pointer (shrink the window)
            - else shift the right pointer (expand until we have a valid substring)
        - return the final result

        - how to check if window contains all chars from t and avoid repeating work each iteration?
            only look at chars in the s window that are also in the t window, 
            keep an int of how many chars we have satisfied vs how many we need,
            when we add a relevant char to the s table, increment the have int if it reached the count required,
            and vice versa when removing a char from the s table

        - time: n for one pass with a constant time check of the have vs need counts
        """
        if len(s) < len(t) or t == "":
            return ""
        
        resultPtr = [-1, -1]
        resultLength = float("infinity")
        tMap, sMap = {}, {}

        # create the t table
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        haveCount, needCount = 0, len(tMap)

        # iterate through s
        left = 0
        for right in range(len(s)):
            # update the s table with the new char in s
            c = s[right]
            sMap[c] = 1 + sMap.get(c, 0)
            # if c is a relevant char in t and if we satisfied the count for it, update the have vs need
            if c in tMap and tMap[c] == sMap[c]:
                haveCount += 1

            # if the window contains all chars from t (valid window)
            while haveCount == needCount:
                # record result
                curLen = right - left + 1
                if curLen < resultLength:
                    resultPtr = [left, right]
                    resultLength = curLen
                # remove left & update s table & update have vs need
                if s[left] in tMap and tMap[s[left]] == sMap[s[left]]:
                    haveCount -= 1
                sMap[s[left]] -= 1
                left += 1

            # if the window does not contain all chars from t, do nothing

        return s[resultPtr[0]:resultPtr[1]+1] if resultLength != float("infinity") else ""