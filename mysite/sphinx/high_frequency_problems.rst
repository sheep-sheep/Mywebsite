High Frequency Questions
==========================

This section will record all the popular questions and their follow ups during the interviews.

LeetCode 347. Top K Frequent Elements
--------------------------------------------

It seems that the initial problem is not hard, you can have 2 solutions:
    * Using *minHeap* which is O(nlogk)
    * Using *BucketSort* which is O(n)


#. Solution with Dict + Sort

The code below is using bucket sort, and i'm using the *lambda* function to simplify the code::
    class Solution(object):
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            # if we do a mergesort, the time completxisty will be O(nlogn)
            res = dict()

            for num in nums:
                if num in res:
                    res[num] += 1
                else:
                    res[num] = 1
            # lambda is the most used functions during my work
            res_sorted = sorted(res.items(), key=lambda x: x[1])
            return [item[0] for item in res_sorted[-1:-1 - k:-1]]
        # I can't believe i'm so fast that beats 93% of solutions!!!


#. Solution with Heap


#. Follow up--how do you update the K top results in real time?