## Solution: O(log(n)) | O(1)

def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) -1
    while(left<=right):
        mid = (left + right) // 2
        if target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
        else:
            return mid
    return -1