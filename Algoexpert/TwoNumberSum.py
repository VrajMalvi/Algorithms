# solution 1  - two for loops 

def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
        firstNum = array[i]    
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum,secondNum]

    return []

#  Solution 2 - using hist/dictonary (we can also use set datatype)

def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        match = targetSum - num 
        if match in nums:
            return (match, num)

        else:
            nums[num]=True

    return []

# solution 3 - using sorting and pointers

def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) -1
    while(left<right):
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left] , array[right]]

        elif currentSum < targetSum:
            left +=1 

        elif currentSum > targetSum:
            right -= 1
    return []
