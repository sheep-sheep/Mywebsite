
Sorting Algorithms
=======================
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.
 
Merge Sort
------------
This is the basic method i should master, the top-down merge_sort implementation::

    def merge_sort(nums):
        def merge(leftnums, rightnums):
            i,j = 0,0
            res = []
            while(i<len(leftnums) and j <len(rightnums)):
                if leftnums[i]<rightnums[j]:
                    res.append(leftnums[i])
                    i += 1
                else:
                    res.append(rightnums[j])
                    j += 1
            while(i<len(leftnums)):
                res.append(leftnums[i])
                i += 1
            while (j < len(rightnums)):
                res.append(rightnums[j])
                j += 1
            return res
        if len(nums)==1:
            return nums

        mid = len(nums)/2
        leftnums = merge_sort(nums[:mid])
        rightnums = merge_sort(nums[mid:])
        return merge(leftnums, rightnums)