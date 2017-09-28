Coding Questions - Arrays
===========================
This page will collect all the **array** related questions.


Binary Search
--------------------------

There're 2 ways to implement the simplest binary search on a sorted array::

        def binary_search(nums, lo, hi, target):
            if lo > hi:
                return lo
            mid = (lo+hi)>>1
            if nums[mid] == target:
                return mid
            else:
                return binary_search(nums, mid+1, hi, target) if nums[mid] < target else binary_search(nums, lo, mid-1, target)


        def binary_search_stack(nums, target):
            lo, hi = 0, len(nums)-1
            while lo < hi: # since it's array, we don't need to use while True to keep it loop
                mid = (lo+hi)>>1
                if nums[mid] == target:
                    lo = mid
                    break
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo




LeetCode 189. Rotate Array
-------------------------------------

After i tried so many different solutions, i can't believe the real answer is so simple.


My initial solution with failures::

        class Solution(object):
            def rotate(self, nums, k):
                # Swap the last k elements with the first k elements.
                # The last k elements will be in the correct positions
                # but we need to rotate the remaining (n - k) elements
                # to the right by k steps.
                k = k%len(nums)
                def helper(nums, k):
                    for i in range(k):
                        nums[i], nums[len(nums)-k+i] = nums[len(nums)-k+i], nums[i]
                    for i in range(k):
                        start = k+i
                        end = len(nums)-k+i
                        for j in range(end, start, -1):
                            nums[j], nums[j-1] = nums[j-1], nums[j]
                if k < len(nums)/2:
                    helper(nums, k)
                else:
                    nums = nums[len(nums)/2:] + nums[:len(nums)/2]
                    for i in range(k-len(nums)/2):
                        for j in range(len(nums)-1):
                            nums[j], nums[j + 1] = nums[j + 1], nums[j]


The expected solution::
        class Solution(object):
            def rotate(self, nums, k):
                def reverseInPlace(nums, start, end):
                    while start<end:
                        nums[start], nums[end] = nums[end], nums[start]
                        start += 1
                        end -= 1

                k = k % len(nums)
                reverseInPlace(nums, 0, len(nums)-1)
                reverseInPlace(nums, 0, k-1)
                reverseInPlace(nums, k, len(nums)-1)


