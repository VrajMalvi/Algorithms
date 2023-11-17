# return all possible combinations of 3 element that results in target sum
# in acending order

# Solution 1 :
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

# Solution 2 :
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        # in case last three element are target sum we need to have two more elements after that so -2
        left = i + 1
        right = len(array)-1
        while (left < right):
            currentsum = array[i] + array[left] + array[right]
            if targetSum == currentsum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentsum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets
