Coding Questions - Strings
===========================
This page will collect all the **string** related questions.
 
LeeCode 115. Distinct Subsequences
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


