if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    l1=[]
    i=0
    while i<n:
        j=0
        while j<i:
            
            if(i==j):
                continue
            elif(i>j):
                continue
            else:
                k=0
                while k<j:
                    if(k==j):
                        continue
                    elif j>k:
                        continue 
                    else:
                        l1.append(i,j,k)
                    k+=1
            j+=1
        i+=1
    print(l1)