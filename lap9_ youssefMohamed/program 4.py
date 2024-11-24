def spiral_order(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append(matrix[0][i])
    for i in range( 1,len(matrix)):
        result.append(matrix[i][-1])
    for i in range(len(matrix) - 2, 0, -1):
        result.append(matrix[-1][i])
    for i in range(len(matrix[0]) - 1, 1, -1):
        result.append(matrix[i][0])
    for i in range(1, len(matrix) - 1):
        result.append(matrix[i][0])
    for i in range(1, len(matrix[0]) - 1):
        result.append(matrix[1][i])
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

print(spiral_order(matrix))