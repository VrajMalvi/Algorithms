# return all possible combinations of 3 element that results in target sum in acending order
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    current = 0
    output = []
    while current < (len(array) - 1):
        left = current + 1
        right = len(array) - 1
        while (left < right):
            cs = array[left] + array[current] + array[right]
            if targetSum == cs:
                output.append([array[current], array[left], array[right]])
                left += 1
                right -= 1
            elif cs < targetSum:
                left += 1
            else:
                right -= 1
        current += 1
    return output
