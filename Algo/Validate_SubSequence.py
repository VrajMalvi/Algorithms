# Validate sequence 
"""This is a problem that asks us to create a function that will check to see if a sequence of numbers is a subsequence of a given array.

A subsequence of an array is a set of integers that don’t have to be adjacent in the given array but are in the same order as they appear in the array.

For example, given an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], a valid subsequence would be [2,4,6,8,10]. The numbers aren’t directly next to each other, but they are in the same order as when these integers were in the original array.

Something to note is that a single number in an array and the array itself are both valid subsequences of a given array input. """


# Solution 1 - two pointers to two arrays from the start and moving forward in sequence

def isValidSubsequence(array, sequence):
    # Write your code here.
    arrId = 0
    seqId = 0

    while arrId < len(array) and seqId < len(sequence):
        if array[arrId] == sequence[seqId]:
            seqId +=1
        arrId +=1
    return seqId == len(sequence)
        
# Solution 2 - 

def isValidSubsequence(array, sequence):
    # Write your code here.
    seqId = 0
    for value in array:
        if seqId == len(sequence):
            break # or you can return True
        if sequence[seqId] == value:
            seqId +=1
    return seqId == len(sequence)
