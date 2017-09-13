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
                if pairs[j][1] < pairs[j-1][0]:
                    curr = i
                    pairs[j][1], pairs[i][0] = pairs[i][0], pairs[j][1]
        return curr+1

After sorting, the problem has changed. We can use the sorted result to help us on the solution.

I can add some dp logic here::

        if len(pairs) == 1:
            return 1
        elif len(pairs) == 2:
            return 2 if pairs[1][0] > pairs[0][1] else 1
        else:
            dp = [(0, [0, 0])]
            for i, item in enumerate(pairs):
                dp.append((1, item))
            for n in (2, len(pairs)+1):
                dp[n] = (dp[n-1][0]+1, pairs[n-1]) if pairs[n-1][1] > dp[n-2][1][0] else dp[n-2]

