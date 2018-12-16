Interval Questions
======================================

Meeting Room I, II
------------------------

Merge Intervals, Insert Interval
-----------------------------------
Put them into 3 parts!
Think about the condition when 2 overlaps
Sort can help simplify the condition



Find least number of intervals from A that can fully cover B
-------------------------------------------------------------------

# Given a list of intervals A and one interval B, find the least
# number of intervals from A that can fully cover B.
#
# If cannot find any result, just return 0;
#
# For example:
# Given A=[[0,3],[3,4],[4,6],[2,7]] B=[0,6] return 2 since we can use [0,3] [2,7] to cover the B
# Given A=[[0,3],[4,7]] B=[0,6] return 0 since we cannot find any interval combination from A to cover the B


Greedy: choose furthest range

sort by start, upon same, by end(not necessary)
find eligible intervals for start: base start = target.start
definition of eligible intervals: x is eligible if x.start <= start && x.end > start
special case: if the earliest start > start, no ans, break!!!
Among all eligible intervals, choose the one that has the furthest range
count++;
if(furthest range >= target.end) -> ans found
update start to furthest range
repeat the iteration

Solution::

        def findMinIntervals(intervals, target):
            """
            :type intervals: List[[int, int]]
            :type target: list[int, int]
            :rtype: int
            """
            intervals.sort()
            res = 0
            cur_target = target[0]
            i = 0
            max_step = 0
            while i < len(intervals) and cur_target < target[1]:
                if intervals[i][0] > cur_target:
                    return 0

                while i < len(intervals) and intervals[i][0] <= cur_target:
                    max_step = max(max_step, intervals[i][1])
                    i += 1
                cur_target = max_step
                res += 1
            return res if cur_target >= target[1] else 0
