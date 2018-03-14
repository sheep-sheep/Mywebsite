Palindromic String
=================================


LeetCode 5. Longest Palindromic Substring
---------------------------------------------

Solutions::

        class Solution(object):
            def longestPalindrome_0(self, s):
                """
                :type s: str
                :rtype: str
                """
                if s == s[::-1]:
                    return s
                # len of palindromic substring starting from
                dp = [[False for i in range(len(s) + 1)] for j in range(len(s) + 1)]
                start = 0
                maxlen = 0
                for i in range(len(s), 0, -1):  # [N, ..., 1]
                    for j in range(i, len(s) + 1):
                        if i == j or i + 1 == j:
                            dp[i][j] = s[i - 1] == s[j - 1]
                        else:
                            dp[i][j] = s[i - 1] == s[j - 1] and dp[i + 1][j - 1]

                        if dp[i][j] and j - i > maxlen:
                            maxlen = j - i
                            start = i - 1

                return s[start: start + maxlen + 1]

            def longestPalindrome(self, s):
                res = ""
                for i in xrange(len(s)):
                    # odd case, like "aba"
                    tmp = self.helper(s, i, i)
                    if len(tmp) > len(res):
                        res = tmp
                    # even case, like "abba"
                    tmp = self.helper(s, i, i + 1)
                    if len(tmp) > len(res):
                        res = tmp
                return res

            # get the longest palindrome, l, r are the middle indexes
            # from inner to outer
            def helper(self, s, l, r):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1;
                    r += 1
                return s[l + 1:r]


LeetCode 647. Palindromic Substrings
-------------------------------------------

My first thought is to use permutation

Solutions::


        class Solution(object):
            def countSubstrings(self, s):
                """
                :type s: str
                :rtype: int
                """
                # when think up the DP solution, DP will stand for True/False instead of number of palindrome.
                # It's because when you set it to #, it's very hard to build the relationship between N and N-1.
                if len(s) == 0:
                    return 0
                N = len(s)
                dp = [[1 if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]
                count = 0
                for i in range(1, N+1):
                    for j in range(i, 0, -1):
                        # since we need next pos's info to decide current info, we can't use ascending order, we need
                        # descending order
                        if i == j:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = 1 if (s[i - 1] == s[j - 1]) and (dp[i - 1][j + 1] or j+1==i) else 0
                        print dp
                        if dp[i][j]:
                            count += 1
                return count