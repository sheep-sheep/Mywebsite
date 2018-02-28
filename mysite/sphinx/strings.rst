Coding Questions - Strings
===========================
This page will collect all the **string** related questions.

Tips in Python
----------------------------------------
#. '1'.isdigit() will return True or False
#. num += num*10 + ('digit'-'0') will convert a string to an integer during the traverse


LeetCode 115. Distinct Subsequences
----------------------------------------

* empty string is a subsequence of any string but only 1 time
* use dp[i][j] to denote # of times the string s[0:j] contains the string t[0:i]

        +---+---+---+---+-----+---+
        |   | 0 | 1 | 2 | ... | j |
        +===+===+===+===+=====+===+
        | 0 | 1 | 1 | 1 | ... | 1 |
        +---+---+---+---+-----+---+
        | 0 | 0 | 0 | 0 | ... | 0 |
        +---+---+---+---+-----+---+
        |...| 0 | 0 | 0 | ... | 0 |
        +---+---+---+---+-----+---+
        | i | 0 | 0 | 0 | ... | 0 |
        +---+---+---+---+-----+---+           


The key point in DP solution is to clarify the different meaning of index number
between dp[i] and str[i].


:dp[i][j]:        represents the # of distinct results between S[0:**j-1**] and T[0: **i-1**]
:dp[i][j-1]:      represents the # of distinct results between S[0:**j-2**] and T[0: **i-1**]
:dp[i-1][j-1]:    represents the # of distinct results between S[0:**j-2**] and T[0: **i-2**]

* Usually we initialize the dp array with N+1 space, the extra space is to handle corner cases
* When you use the loop to create dp array, the outer loop is for row and inner loop is for col.
* Always put the status that keeps changing in inner loop which is S[j] in this question

This is the source code::

    def numDistinct(self, s, t):
        # create extra space for the 0 condition
        dp = [[0 for _ in range(len(s) + 1)] for __ in range(len(t) + 1)]

        # Initialize the dp array
        for i in range(len(s) + 1):
            dp[0][i] = 1

        # keep outer loop still, increase the inner loop which is string s
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                dp[i][j] = dp[i][j - 1] if s[j - 1] != t[i - 1] else dp[i - 1][j - 1] + dp[i][j - 1]
        return dp[-1][-1]



LeetCode 91. Decode Ways
----------------------------

:dp[i]:     represents the # of decode ways for string S[:**i-1**], the last char
:dp[i-1]:   represents the # of decode ways for string S[:**i-2**], the last 2nd char
:dp[i-2]:   represents the # of decode ways for string S[:**i-3**], the last 3rd char

* if S[i-2:i] is 2 digits, then it has 2 ways:
                #. S[:i-2]'s ways + S[i-2:i]
                #. S[:i-1]'s ways + S[i-1:i]
* if S[i-2:i] isn't 2 digits, then it only has one decode way:
                #. S[:i-1]'s ways + S[i-1:i]

Then the final relationship will be::

    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == '':
            return 0
        dp = [1] + [0] * (len(s))
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':  # this is to handle "10" and "01"ways = 0
                dp[i] += dp[i-2]
        return dp[-1]

String Pattern Search
=====================================

After deal with so many string problems, we can take a look at several classic as well as brilliant algorithms.

1. Brute Force
    Check the pattern at each position

2. Knuth-Morris-Pratt
    There 2 ways to implement KMP: 
        1) using DFA to build a state table
        2) using prefix function to build a table based on pattern itself!
    
3. Boyer-Moore
    Skip the checked position
4. Rabin-Karp
    Use hash function to encode the pattern

If you want to find some common characteristics, that's to avoid back up as much as possible!

**5. Sliding window problems**
