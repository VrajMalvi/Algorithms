# O(N^2) time | O(1) - Space
# Bubble sort works by repeatedly stepping through the list, 
# comparing each pair of adjacent items and swapping them if they are 
# in the wrong order, until the entire list is sorted.

def bubbleSort(array):
    # Write your code here.
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array

def swap(i, j , array):
    array[i], array[j] = array[j], array[i]
