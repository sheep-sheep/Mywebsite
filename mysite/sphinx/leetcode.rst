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

No, it doesn't look right, the real DP should look like:
* LIS(i) =   1 + max(LIS(j)) if A[i]>A[j] for 1<j<i
* Or     =   1 if no such j exists.

source code::
    # this is Recursion
    class Solution(object):
        overallMax = 1
        def lengthOfLIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # according to the description, come up with the solution that use recursion
            def helper(array, n):
                # this helper method will return # of LIS ending at n-1
                if len(array)==1:
                    return 1
                currMax = 1
                for i in range(1, n):
                    res = helper(array, i)
                    if array[i-1] < array[n-1] and res+1 > currMax:
                        currMax = res +1

                self.overallMax = max(self.overallMax, currMax)
                return currMax
            if len(nums) == 0:
                return 0
            helper(nums, len(nums))
            return self.overallMax

    # then we can convert this logic to DP
    class Solution(object):
        def lengthOfLIS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # dp[i] denote the # of LIS ending at i-1
            dp = [0] + [1]*len(nums)

            for i in range(1, len(nums)+1):
                currMax = 1
                for j in range(1, i):
                    if nums[j-1] < nums[i-1]:
                        currMax = max(currMax, dp[j] + 1)
                dp[i] = currMax
            return max(dp)

    # Could you improve it to O(n log n) time complexity?
    class Solution(object):
        def lengthOfLIS(self, nums):
            def binary_search(nums, lo, hi, target):
                if lo > hi:
                    return lo
                mid = (lo + hi) >> 1
                if nums[mid] == target:
                    return mid
                else:
                    return binary_search(nums, mid + 1, hi, target) if nums[mid] < target else binary_search(nums, lo, mid - 1, target)

            dp = [0] * len(nums)
            res = 0 # length of the sequence res + 1
            for num in nums:
                pos = binary_search(dp, 0, res-1, num)
                dp[pos] = num
                res = max(pos + 1, res) # will always record the max pos of tails
            return res

It seems that i'm not used to the DP that needs additional operation at each DP step.



LeetCode 354. Russian Doll Envelopes
---------------------------------------------------
There're 2 tips learnt from this question:
    #. sorted built-in method
    #. the binary search method for LIS problem


Naive and final solution are as followings::
    class Solution(object):
        def maxEnvelopes(self, envelopes):
            # [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting, 
            # otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
            nums = sorted(envelopes, key = lambda x: (x[0], -x[1])) # sorted will create a new list
            
            # dp[i] denote the # of LIS ending at i-1
            dp = [0] + [1]*len(nums)
            # The LIS DP solution got TLE, i need to use Binary Search solution.
            for i in range(1, len(nums)+1):
                currMax = 1
                for j in range(1, i):
                    if nums[j-1][1] < nums[i-1][1]:
                        currMax = max(currMax, dp[j] + 1)
                dp[i] = currMax
            return max(dp)


    



LeetCode 491. Increasing Subsequences
---------------------------------------------------

# Solution 1, to do a brute force traverse for each situation, you can have a window from 2 to max Len, and fill each element in that
    window

# Solution 2, it relates to the ending position and it also relates to the number of permutation, ah ha, this is a BackTracking issue and not DP, don't be fooled!

Solution is::
    class Solution(object):
        def findSubsequences(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            # start with a simple permutation problem
            # then add constraints when adding combination
            # filter out the smaller pair
            def checkIncreasing(nums, target):
                for i in range(1, len(nums)):
                    if nums[i] < nums[i-1]:
                        return False
                return True

            def helper(nums):
                if len(nums) == 1:
                    return [nums]
                res = []
                for i in range(len(nums)):
                    res.append([nums[i]])
                    for item in helper(nums[i+1:]):
                        if nums[i] <= item[0] and checkIncreasing(item, nums[i]):
                            res.append([nums[i]] + item)
                return res
            res = set([tuple(item) for item in helper(nums) if len(item)>1])
            return list(res)

    # Don't need to check each item
    class Solution(object):
        def findSubsequences(self, nums):
            def helper(nums):
                if len(nums)==1:
                    return [nums]
                if len(nums)==2:
                    return [[nums[0]], [nums[1]], nums] if nums[0]<=nums[1] else [[nums[0]], [nums[1]]]
                res = []
                for i in range(len(nums)):
                    res.append([nums[i]])
                    for item in helper(nums[i+1:]):
                        if nums[i] <= item[0]:
                            res.append([nums[i]] + item)
                return res
            res = set([tuple(item) for item in helper(nums) if len(item)>1])
            return list(res)




