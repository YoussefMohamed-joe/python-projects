

def generate_matrix(n): 
    result=[[0 for i in range(n)] for j in range(n)]
    counter=1
    upper=0
    lower=n-1
    left=0
    right=n-1
    while  left <= right and upper <= lower:
        for i in range(left, right + 1):
            result[upper][i] = counter
            counter += 1
        upper += 1

        for i in range(upper, lower + 1):
            result[i][right] = counter
            counter += 1
        right -= 1

        for i in range(right, left - 1, -1):
            result[lower][i] = counter
            counter += 1
        lower -= 1

        for i in range(lower, upper - 1, -1):    
            result[i][left] = counter
            counter += 1
        left += 1        
        
        
    return result




n=int(input("please enter your number: "))
print(generate_matrix(n))