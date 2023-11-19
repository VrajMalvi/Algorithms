# find the absolute smallest difference between elements of two array
# for ex abs diff of -5 and 5 would be 10
# for ex abs diff of -5 and -4 would be 1

# Solution:

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstnum = arrayOne[idxOne]
        secondnum = arrayTwo[idxTwo]
        if firstnum < secondnum:
            current = secondnum - firstnum
            idxOne += 1
        elif secondnum < firstnum:
            current = firstnum - secondnum
            idxTwo += 1
        else:
            return [firstnum, secondnum]
        if smallest > current:
            smallest = current
            smallestPair = [firstnum, secondnum]
    return smallestPair
