def sumtime(arr, row, col):
    sum = 0
    sum += arr[row - 1][col - 1]
    sum += arr[row - 1][col]
    sum += arr[row - 1][col + 1]
    sum += arr[row][col]
    sum += arr[row + 1][col - 1]
    sum += arr[row + 1][col]
    sum += arr[row + 1][col + 1]

    return sum


# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxsofar = -63
    for i in range(1, 5):
        for j in range(1, 5):
            sumnow = sumtime(arr, i, j)
            if sumnow > maxsofar:
                maxsofar = sumnow
    return maxsofar