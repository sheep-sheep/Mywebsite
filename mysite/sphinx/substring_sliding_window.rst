SubString Searching Problem with Sliding Window Solutions
===============================================================

LeetCode 438. Find All Anagrams in a String
---------------------------------------------

Sliding window, does it have something to do with KMP? i find some logic are the same.

Solution::

        class Solution(object):
            def findAnagrams(self, s, p):
                # create a bucket table for p which contains number of occurrences.
                helper = dict()
                for char in p:
                    helper[char] = helper[char]+1 if char in helper else 1
                # number of distinct char
                count = len(helper)
                begin = end = 0
                res = []

                while end < len(s):
                    if s[end] in helper:
                        helper[s[end]] -= 1
                        if helper[s[end]]==0:
                            count -= 1
                    end += 1

                    # count is 0 means we have reached a pos that [begin, end) has all the
                    # possible chars in p
                    # next step is to check whether the [begin, end) is a valid sub-string
                    while count == 0:
                        if s[begin] in helper:
                            helper[s[begin]] += 1
                            if helper[s[begin]] > 0:
                                count += 1
                        # when the len doesn't match means we have extra chars
                        # the number of extras will be captured by helper[s[begin]] += 1
                        if end - begin == len(p):
                            res.append(begin)
                        begin += 1  # we will need the prev begin char to fill the new end position

                return res

LeetCode 76. Minimum Window Substring
----------------------------------------------                

        class Solution(object):
            def minWindow(self, s, t):
                s = list(s)
                helper = {}
                for c in t:
                    helper[c] = helper.get(c, 0) + 1

                begin = 0
                end = 0
                head = 0
                counter = len(helper)
                maxLen = float('inf')
                res = ''
                while end < len(s):
                    if s[end] in helper:
                        helper[s[end]] -= 1
                        if helper[s[end]] == 0:
                            counter -= 1
                    end+=1
                    
                    while counter == 0:
                        if s[begin] in helper:
                            helper[s[begin]] += 1
                            if helper[s[begin]] > 0:
                                counter += 1
                        if end - begin < maxLen:
                            maxLen = end - begin
                            head = begin
                        begin += 1
                        
                if maxLen == float('inf'):
                    return ''
                else:
                    return ''.join(s[head: head+maxLen])


LeetCode 340. Longest Substring with At Most K Distinct Characters
--------------------------------------------------------------------------

Solution::
        
        class Solution(object):
            def lengthOfLongestSubstringTwoDistinct(self, s, k):

                s = list(s)
                helper = {}
                begin = 0
                end = 0
                maxLen = 0
                count = 0
                
                while end < len(s):    
                    if s[end] not in helper:
                        count += 1
                        helper[s[end]] = 1
                    else:
                        helper[s[end]] += 1
                    end += 1
                    
                    while count > k:
                        helper[s[begin]] -= 1
                        if helper[s[begin]] == 0:
                            count -= 1
                            del helper[s[begin]]
                        begin += 1
                    maxLen = max(maxLen, end-begin)
                return maxLen                

LeetCode 424. Longest Repeating Character Replacement
----------------------------------------------------------



LeetCode 3. Longest Substring Without Repeating Characters
---------------------------------------------------------------------          
Solution::
        
        class Solution(object):
            def lengthOfLongestSubstring(self, s):
                s = list(s)
                helper = {}
                begin = 0
                end = 0
                count = 0
                maxLen = 0
                while end < len(s):
                    if s[end] not in helper:
                        helper[s[end]] = 1
                    else:
                        helper[s[end]] += 1
                        count += 1
                    end += 1
                    
                    while count > 0:
                        if helper[s[begin]] > 1:
                            count -= 1
                        helper[s[begin]] -= 1
                        if helper[s[begin]] == 0:
                            del helper[s[begin]]
                        begin += 1
                    maxLen = max(maxLen, end - begin)
                return maxLen  


LeetCode 424. Longest Repeating Character Replacement
----------------------------------------------------------

Solution::
        class Solution(object):
            def characterReplacement(self, s, k):
                """
                :type s: str
                :type k: int
                :rtype: int
                """
                helper = {}
                begin = 0
                end = 0
                frequency = 0
                res = 0
                # (length of substring - number of times of the maximum occurring character in the substring) <= k
                while end < len(s):
                    if s[end] in helper:
                        helper[s[end]] += 1
                    else:
                        helper[s[end]] = 1
                    frequency = max(frequency, helper[s[end]])
                    
                    if end - begin - frequency + 1> k:
                        helper[s[begin]] -= 1
                        begin += 1    
                    res = max(res, end-begin+1)
                    end += 1
                return res

LeetCode 30. Substring with Concatenation of All Words
--------------------------------------------------------------

TOO Complicated, give up for now.