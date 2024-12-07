def spiral_order(matrix,n):
    result = []
    upper=0
    lower=n-1
    left=0
    right=n-1
    while  left <= right and upper <= lower:
        for i in range(left, right + 1):
            result.append(matrix[upper][i])
        upper += 1

        for i in range(upper, lower + 1):
            result.append(matrix[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            result.append(matrix[lower][i])
        lower -= 1

        for i in range(lower, upper - 1, -1):    
            result.append(matrix[i][left])
        left += 1
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

print(spiral_order(matrix,3))