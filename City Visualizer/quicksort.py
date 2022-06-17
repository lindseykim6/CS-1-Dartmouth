# File Name: quicksort.py
# Author Name: Lindsey Kim
# Date: 11/2/2020
# Course: COSC 1
# Short Description: This sorts the list by using partitions
#

# partitions the list by moving the numbers that are less than the pivot before it and moving the numbers that are
# greater than the pivot after it
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]  # the last element in the list
    i = p-1  # the index of where the partition is between the numbers below the pivot and the pivot
    j = p  # the index of where the partition is between the numbers above the pivot and the unsorted numbers
    while j != r:  # ends when j reaches the index below the last one
        if compare_func(the_list[j], pivot):  # if the element at j is less than or equal to the pivot
            i += 1
            (the_list[i], the_list[j]) = (the_list[j], the_list[i])  # switch elements at index i and j
        j += 1
    (the_list[r], the_list[i+1]) = (the_list[i+1], the_list[r])  # switch elements at index i+1 and r
    return i+1


def quicksort(the_list, p, r, compare_func):
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)  # recursively partitions the list
        quicksort(the_list, q+1, r, compare_func)


def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)  # sorts the entire list
