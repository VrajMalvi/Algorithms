# solution
def transposeMatrix(matrix):
    # Write your code here.
    transposeMatrix = []
    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        transposeMatrix.append(temp)
    return transposeMatrix