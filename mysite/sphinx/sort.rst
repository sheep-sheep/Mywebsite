
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
        
        i write megersort, buble sort, insertion sort and selection sort today.
        
        however, computer crashes!!! damn!


# Another placeholder for sorting algorithm:

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
