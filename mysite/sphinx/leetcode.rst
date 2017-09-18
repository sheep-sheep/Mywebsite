LeetCode 646. Maximum Length of Pair Chain
---------------------------------------------------

My initial thought is to use Insertion sort, because the sort
will always keep a sorted list and the list will be the chain.

However, the insertion won't help us achieve the max length, it can only
assure the pairs are in an order.

source::
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        curr = 0
        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                if pairs[j][1] < pairs[i][0]:
                    curr = i
                    pairs[j][1], pairs[i][0] = pairs[i][0], pairs[j][1] # problem here! we shouldn't break each pair!
        return curr+1

After sorting, *sort on Pair[0] or Pair[1]* will give us different approach. Now, the problem has changed. We can use the sorted result to help us on the solution.

My initial thought is to use DP, however, i met some difficulties::

        # initialize the dp
        dp = []
        for i, item in enumerate(pairs):
            dp.append((1, item))

        for n in range(1, len(pairs)):
            if n == 1:
                dp[n] = (2, pairs[1]) if pairs[1][0] > pairs[0][1] else (1, pairs[0])
            else:
                dp[n] = (dp[n-1][0]+1, pairs[n]) if pairs[n][0] > dp[n-1][1][1] else dp[n-1]
        return dp[-1][0]

The above solution doesn't look like a regular DP solution becasue the index and the meaning of DP is not clear.


In fact the problem seems much simpler that i thought, you will just need to keep find the element
that is larger than the last element.

Then we will just need one variable to hold the state::

        curr = pairs[0]
        count = 1
        for pair in pairs:
            if pair[0] > curr[1]:
                curr = pair
                count += 1

But with above solution i got TLE error which means i need a faster way to sort the list.

I'm thinking about the python map or lambda function::

    class Solution(object):
        def findLongestChain(self, pairs):
            """
            :type pairs: List[List[int]]
            :rtype: int
            """
            if not pairs:
                return 0
            pairs = sorted(pairs, key=lambda x: x[1])
            curr = pairs[0]
            count = 1
            for pair in pairs:
                if pair[0] > curr[1]:
                    curr = pair
                    count += 1
            return count
    # also because we were sorting x[1], we will need to use x[0] to do check, vice versa.

:dp[i]:        represents the # of chain pairs for Pairs[0, ..., i-2, i-1]
:dp[i-1]:      represents the # of chain pairs for Pairs[0, ..., i-2]

* dp[i] = dp[i-1] + 1 if Pairs[i-1][0]>last[1] else dp[i-1]

Be careful about the initilization with mulitple states::
    class Solution(object):
        def findLongestChain(self, pairs):
            """
            :type pairs: List[List[int]]
            :rtype: int
            """
            pairs = sorted(pairs, key=lambda x: x[1])
            # dp[i] = dp[i-1] + 1 if Pairs[i-1][0]>last[1] else dp[i-1]
            dp = [0] + [1]*len(pairs)
            curr = [float('-inf'), float('-inf')] # initialize the dp[0] min pair
            for i in range(1, len(pairs)+1): # starting with 1 is to make sure Pairs[i-1] is valid
                if pairs[i - 1][0] > curr[1]:
                    dp[i] = dp[i-1] + 1
                    curr = pairs[i - 1]
                else:
                    dp[i] = dp[i-1]
            return dp[-1]


LeetCode 300. Longest Increasing Subsequence
---------------------------------------------------

This is more complex than the LongestChainPair problem which can be simplified by sorting the array.
The hard part of this problem is that the longest subsequence might change according to different current number,
thus you need to evaluate the whole array again to make sure you can the optimal answer.

Then the newest logic should be for each value, we need to find the # of values smaller that itself and compare the count::
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        dp = [0] + [1] * len(nums)
        for i in range(1, len(nums)+1):
            if not s or nums[i-1] > s[-1]:
                s.append(nums[i-1])
                dp[i] = len(s)
            else:
                for j in range(len(s)-1, -1, -1):
                    if nums[i-1] <= s[j]:
                        end = j
                tmp = s[:end]+[nums[i-1]]
                if len(s) <= len(tmp):
                    s = tmp
                dp[i] = len(s)
        return max(dp), s


LeetCode 491. Increasing Subsequences
---------------------------------------------------