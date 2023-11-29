# Solution:
# O(n) | O(n)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    calculateSum(root, 0, sums)
    return sums


def calculateSum(root, runningSum, sums):
    if root is None:
        return []

    newRunningSum = runningSum + root.value
    if root.left is None and root.right is None:
        sums.append(newRunningSum)
        return

    calculateSum(root.left, newRunningSum, sums)
    calculateSum(root.right, newRunningSum, sums)
