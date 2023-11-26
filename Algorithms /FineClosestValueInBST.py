# solution 1:
# Avg: O(log(n)) time | O(log(n)) space
# worst case: O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestvalueBstHelper(tree, target, float('inf'))


def findClosestvalueBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestvalueBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestvalueBstHelper(tree.right, target, closest)
    else:
        return closest
    
# Solution 2:
# Avg: O(log(n)) time | O(1) space
# worst case: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestvalueBstHelper(tree, target, float('inf'))

def findClosestvalueBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest