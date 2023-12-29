# O(n^2) time | O(1) space
# Insertion Sort is a simple sorting algorithm 
# that builds the final sorted array one element at a time. 

def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
