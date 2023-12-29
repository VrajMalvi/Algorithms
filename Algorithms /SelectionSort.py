# time O(N^2) | space O(1)
# The term "selection sort" refers to a simple sorting algorithm that works 
# by repeatedly selecting the minimum (or maximum) element from 
# the unsorted portion of 
# the array and putting it at the beginning (or end) of the sorted portion.
def selectionSort(array):
    # Write your code here.
    currentIdx = 0
    while currentIdx < len(array) -1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
