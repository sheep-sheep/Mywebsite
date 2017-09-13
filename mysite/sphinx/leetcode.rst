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